import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.simple_agent import SimpleAgent
from core.session import Session
from core.reasoning_trace import ReasoningTrace
from connectors.arcanea_memory_loader import load_lore


def test_agent_interaction(tmp_path):
    session = Session()
    agent = SimpleAgent(session=session)
    response = agent.interact(["Hello", "world"])
    assert response == "Hello | world"
    trace = agent.trace()
    assert "USER: Hello" in trace
    assert "ASSISTANT: Hello | world" in trace


def test_load_lore(tmp_path):
    # Create temporary markdown file
    lore_file = tmp_path / "lore.md"
    lore_file.write_text("Lore text")
    data = load_lore(str(tmp_path))
    assert data == ["Lore text"]
