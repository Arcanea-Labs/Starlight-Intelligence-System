"""Reasoning trace builder.

Provides helper functions to assemble and represent reasoning traces.
A reasoning trace records the intermediate steps an agent takes to
arrive at a conclusion.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class TraceStep:
    """A single step in a reasoning trace."""

    message: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ReasoningTrace:
    """Collection of ``TraceStep`` objects."""

    steps: List[TraceStep] = field(default_factory=list)

    def add_step(self, message: str) -> None:
        """Append a reasoning step to the trace."""
        self.steps.append(TraceStep(message=message))

    def to_dict(self) -> List[dict]:
        """Return the trace as a list of serializable dictionaries."""
        return [
            {"message": step.message, "timestamp": step.timestamp.isoformat()}
            for step in self.steps
        ]


class TraceBuilder:
    """Helper for building reasoning traces programmatically."""

    def __init__(self) -> None:
        self.trace = ReasoningTrace()

    def record(self, message: str) -> None:
        """Record a reasoning message."""
        self.trace.add_step(message)

    def build(self) -> ReasoningTrace:
        """Return the constructed reasoning trace.

        Example
        -------
        >>> tb = TraceBuilder()
        >>> tb.record("Analyze lore entry")
        >>> tb.record("Synthesize response")
        >>> trace = tb.build()
        >>> print(trace.to_dict())
        """
        return self.trace


