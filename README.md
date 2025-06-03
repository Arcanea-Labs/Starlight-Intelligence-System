# Starlight Intelligence System

The Starlight Intelligence System (SIS) powers reasoning, memory storage, and agent orchestration for World building projects like the Arcaea projects It acts as the brain and memory core that you can use to leverage the insights of your reasoning with LLMs and ensure you build a system and create value through your thought. 


SIS enables long-term reasoning, daily thought logging, and AI agent memory. Arcanea provides a universe and lore memory layer that connects to SIS through custom loaders.


## Repository Structure
- **starlight-notes/** - Markdown-based reasoning logs.
- **templates/** - Note templates and agent prompt scaffolds.
- **agents/** - Agent configurations and flows (ADK, LangChain, CrewAI, etc.).
- **connectors/** - Loaders for external knowledge sources, e.g., `arcanea_memory_loader.py`.
- **core/** - Memory engine, reasoning trace builder, and session controller.

SIS is the backend reasoning and publishing system used by Arcanea and future applications.
