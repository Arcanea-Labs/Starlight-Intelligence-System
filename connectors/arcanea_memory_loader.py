"""Load Arcanea lore or memory files into SIS sessions."""

from __future__ import annotations

from pathlib import Path
from typing import List


def load_lore(directory: str) -> List[str]:
    """Load markdown or text files from a lore directory."""
    texts: List[str] = []
    for path in Path(directory).glob("*.md"):
        texts.append(path.read_text())
    for path in Path(directory).glob("*.txt"):
        texts.append(path.read_text())
    return texts
