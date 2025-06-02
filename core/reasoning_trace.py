"""Utilities to build reasoning traces from sessions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .session import Session

@dataclass
class ReasoningTrace:
    """Builds a reasoning trace from a session."""

    session: Session

    def build(self) -> str:
        """Return a concatenated reasoning trace from the session."""
        return "\n".join(self.session.trace())
