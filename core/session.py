"""Session controller for building reasoning traces."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Iterable

from .memory import MemoryStore

@dataclass
class Session:
    """Represents a reasoning session."""

    store: MemoryStore = field(default_factory=MemoryStore)

    def log(self, text: str) -> None:
        """Log text to the session's memory store."""
        self.store.add(text)

    def trace(self) -> Iterable[str]:
        """Return an iterator over the session reasoning trace."""
        return self.store.get_all()
