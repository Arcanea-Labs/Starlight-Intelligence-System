# Starlight Intelligence System

The Starlight Intelligence System (SIS) powers reasoning, memory storage, and agent orchestration for Arcanea-Labs projects. It acts as the brain and memory core of the Arcanean ecosystem while remaining application-agnostic so it can support apps like Arcanea, FrankX, and Akamoto.

SIS enables long-term reasoning, daily thought logging, and AI agent memory. Arcanea provides a universe and lore memory layer that connects to SIS through custom loaders.

## Repository Structure
- **starlight-notes/** - Markdown-based reasoning logs.
- **templates/** - Note templates and agent prompt scaffolds.
- **agents/** - Agent configurations and flows (LangChain, CrewAI, etc.).
- **connectors/** - Loaders for external knowledge sources, e.g., `arcanea_memory_loader.py`.
- **core/** - Memory engine, reasoning trace builder, and session controller.

SIS is the backend reasoning and publishing system used by Arcanea and future applications.

## Installation and Setup

SIS runs on **Python 3.11+**. Using a virtual environment keeps project dependencies isolated from the rest of your system.

```bash
# clone the repository
git clone https://github.com/your-org/Starlight-Intelligence-System.git
cd Starlight-Intelligence-System

# create and activate a virtualenv
python3.11 -m venv .venv
source .venv/bin/activate

# install Python requirements (none are currently required)
pip install -r requirements.txt  # optional placeholder
```

This basic setup gives you an isolated Python environment to experiment with SIS modules or integrate them in your own projects.

## Example Integration Workflow

An application such as **Arcanea** interfaces with SIS through custom loaders in the `connectors/` directory. A typical flow looks like the following:

1. Arcanea collects user thoughts or world events and writes them to a temporary data store.
2. A loader like `arcanea_memory_loader.py` pushes that information into the SIS memory engine located in `core/`.
3. SIS records the data in `starlight-notes/` and builds reasoning traces for future queries.
4. Arcanea then retrieves summaries or relevant memories from SIS to present back to the user, enabling persistent long-term context.

Other projects can follow a similar pattern by writing their own loaders that translate application data into SIS notes and memory traces.
