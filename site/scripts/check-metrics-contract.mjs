import { promises as fs } from "node:fs";
import path from "node:path";

const repoRoot = path.resolve(process.cwd(), "..");
const ledgerPath = path.join(repoRoot, "metrics", "current.json");
const ledger = JSON.parse(await fs.readFile(ledgerPath, "utf8"));

async function deriveAgentCount() {
  const agentsDir = path.join(repoRoot, "agents");
  const entries = await fs.readdir(agentsDir, { withFileTypes: true });
  let count = 0;
  for (const entry of entries) {
    if (entry.isFile()) {
      if (
        entry.name.endsWith(".md") &&
        entry.name !== "AGENT_REGISTRY.md" &&
        entry.name !== "CODING_AGENTS_REGISTRY.md"
      ) count += 1;
    } else if (entry.isDirectory()) {
      const children = await fs.readdir(path.join(agentsDir, entry.name), {
        withFileTypes: true,
      });
      count += children.filter(
        (child) => child.isFile() && child.name.endsWith(".md"),
      ).length;
    }
  }
  return count;
}

async function deriveSkillCounts() {
  const skillsDir = path.join(repoRoot, "skills");
  const domains = await fs.readdir(skillsDir, { withFileTypes: true });
  let dirCount = 0;
  let flatCount = 0;
  for (const domain of domains) {
    if (!domain.isDirectory()) continue;
    const domainPath = path.join(skillsDir, domain.name);
    const entries = await fs.readdir(domainPath, { withFileTypes: true });
    // A domain may itself be a skill package (e.g. skills/crypto-intelligence/SKILL.md,
    // referenced by rule skill "crypto-intelligence").
    if (entries.some((entry) => entry.isFile() && entry.name === "SKILL.md")) dirCount += 1;
    for (const entry of entries) {
      if (entry.isDirectory()) {
        try {
          await fs.access(path.join(domainPath, entry.name, "SKILL.md"));
          dirCount += 1;
        } catch {
          // Non-skill subfolder
        }
      } else if (
        entry.isFile() &&
        entry.name.endsWith(".md") &&
        entry.name !== "SKILL.md" &&
        entry.name !== "README.md" &&
        entry.name !== "SKILL_REGISTRY.md"
      ) {
        flatCount += 1;
      }
    }
  }
  return { dirCount, flatCount };
}

function value(name) {
  const metric = ledger.metrics?.[name];
  if (!metric || !Number.isFinite(metric.value) || !metric.last_verified || !metric.source || metric.stale) {
    throw new Error(`Metric ${name} must be reproducible, sourced, dated, and non-stale`);
  }
  return metric.value;
}

const agentCount = await deriveAgentCount();
const { dirCount: skillDirCount, flatCount: skillFlatCount } = await deriveSkillCounts();
const skillRules = JSON.parse(
  await fs.readFile(path.join(repoRoot, "skills", "skill-rules.json"), "utf8"),
).rules;
const vaultRegistry = JSON.parse(
  await fs.readFile(path.join(repoRoot, "vault-registry.json"), "utf8"),
);
const publicVaults = Array.isArray(vaultRegistry.vaults)
  ? vaultRegistry.vaults
  : [];
const horizonLetters = (await fs.readFile(
  path.join(repoRoot, "public-vault", "horizon.jsonl"),
  "utf8",
)).split("\n").filter((line) => line.trim()).length;

const observed = {
  registered_agents: agentCount,
  skill_activation_rules: skillRules.length,
  skill_definitions_dir_format: skillDirCount,
  skill_definitions_flat_format: skillFlatCount,
  starlight_vaults: publicVaults.length,
  horizon_letters: horizonLetters,
};

for (const [name, count] of Object.entries(observed)) {
  const claimed = value(name);
  if (claimed !== count) {
    throw new Error(`Metric drift: ${name} claims ${claimed}, source contains ${count}`);
  }
}

console.log("Metrics contract verified:", observed);
