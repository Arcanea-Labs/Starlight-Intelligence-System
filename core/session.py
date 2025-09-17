"""Session controller for building reasoning traces."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Iterable, Optional

from .memory import MemoryStore, MemoryEntry

@dataclass
class Session:
    """Represents a reasoning session."""

    store: MemoryStore

    def __init__(self, store_path: str = ".chroma"):
        self.store = MemoryStore(db_path=store_path)

    def log(self, text: str, entry_type: str, source: Optional[str] = None) -> None:
        """Log text to the session's memory store."""
        entry = MemoryEntry(text=text, entry_type=entry_type, source=source)
        self.store.add(entry)

    def trace(self) -> List[MemoryEntry]:
        """Return the session reasoning trace."""
        return self.store.get_all()
