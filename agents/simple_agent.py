"""Example agent that logs interactions to the SIS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from core.session import Session
from core.reasoning_trace import ReasoningTrace


@dataclass
class SimpleAgent:
    """A minimal agent for demonstration purposes."""

    session: Session
    name: str = "simple_agent"

    def interact(self, messages: Iterable[str]) -> str:
        """Process a list of messages and return a combined response."""
        for msg in messages:
            self.session.log(text=msg, entry_type="user_input", source="user")

        # In a real system, this is where the LLM call would occur
        response = " | ".join(messages)

        self.session.log(text=response, entry_type="agent_response", source=self.name)
        return response

    def trace(self) -> str:
        """Return a simple string representation of the session trace."""
        entries = self.session.trace()
        return "\n".join([f"[{e.entry_type}] {e.text}" for e in entries])
