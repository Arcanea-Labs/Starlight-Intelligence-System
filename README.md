# Starlight Intelligence System

The Starlight Intelligence System (SIS) powers reasoning, memory storage, and agent orchestration for Arcanea-Labs projects. It acts as the brain and memory core of the Arcanean ecosystem while remaining application-agnostic so it can support apps like Arcanea, FrankX, and Akamoto.

SIS enables long-term reasoning, daily thought logging, and AI agent memory. Arcanea provides a universe and lore memory layer that connects to SIS through custom loaders.

This repository contains minimal but functional Python modules illustrating how agents can log reasoning traces and load external lore. Tests demonstrate that these modules integrate correctly.

## Repository Structure
- **starlight-notes/** - Markdown-based reasoning logs.
- **templates/** - Note templates and agent prompt scaffolds.
- **agents/** - Agent configurations and flows (LangChain, CrewAI, etc.).
- **connectors/** - Loaders for external knowledge sources, e.g., `arcanea_memory_loader.py`.
- **core/** - Memory engine, reasoning trace builder, and session controller.

SIS is the backend reasoning and publishing system used by Arcanea and future applications.

## Development

Install dependencies (if any) and run tests with `pytest`:

```bash
pip install -r requirements.txt  # none yet, but placeholder for future deps
pytest -q
```
