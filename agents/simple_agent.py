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

    def interact(self, messages: Iterable[str]) -> str:
        """Process a list of messages and return a combined response."""
        for msg in messages:
            self.session.log(f"USER: {msg}")
        # In a real system, this is where the LLM call would occur
        response = " | ".join(messages)
        self.session.log(f"ASSISTANT: {response}")
        return response

    def trace(self) -> str:
        """Return the reasoning trace built from the session."""
        return ReasoningTrace(self.session).build()
