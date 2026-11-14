import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const ledger = JSON.parse(readFileSync(join(repoRoot, "metrics", "current.json"), "utf8"));

test("site metrics contract passes against the live repository sources", () => {
  const out = execFileSync(process.execPath, ["scripts/check-metrics-contract.mjs"], {
    cwd: join(repoRoot, "site"),
    encoding: "utf8",
  });
  assert.match(out, /Metrics contract verified:/);
});

test("dir-format plus flat-format skill definitions equal the activation rule count", () => {
  const m = ledger.metrics;
  assert.equal(
    m.skill_definitions_dir_format.value + m.skill_definitions_flat_format.value,
    m.skill_activation_rules.value,
  );
});

test("every metric carries a value, ISO verification date, and source", () => {
  for (const [name, metric] of Object.entries(ledger.metrics)) {
    assert.ok(Number.isFinite(metric.value), `${name}.value`);
    assert.match(metric.last_verified, /^\d{4}-\d{2}-\d{2}$/, `${name}.last_verified`);
    assert.ok(metric.source, `${name}.source`);
  }
});
