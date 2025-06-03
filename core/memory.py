"""Simple in-memory storage engine for the Starlight Intelligence System."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

@dataclass
class MemoryEntry:
    """Represents a single piece of stored reasoning or lore."""
    text: str

@dataclass
class MemoryStore:
    """In-memory list-based storage for reasoning entries."""

    entries: List[MemoryEntry] = field(default_factory=list)

    def add(self, text: str) -> None:
        """Add text to the memory store."""
        self.entries.append(MemoryEntry(text=text))

    def get_all(self) -> List[str]:
        """Return all stored text entries."""
        return [e.text for e in self.entries]
