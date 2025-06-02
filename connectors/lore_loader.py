"""Simple lore data loader.

This module demonstrates how to load external lore data from a JSON
file. The loader returns a dictionary representing the lore content.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_lore(path: str | Path) -> Dict[str, Any]:
    """Load lore data from ``path``.

    Parameters
    ----------
    path:
        Path to a JSON file containing lore data.

    Returns
    -------
    dict
        Parsed lore information that can be consumed by other parts of
        the system.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


class LoreLoader:
    """Example loader class for managing lore files."""

    def __init__(self, lore_path: str | Path) -> None:
        self.lore_path = Path(lore_path)

    def load(self) -> Dict[str, Any]:
        """Load and return lore data.

        Example
        -------
        >>> loader = LoreLoader("arcanea_lore.json")
        >>> lore = loader.load()
        >>> print(lore["world"])
        """
        return load_lore(self.lore_path)

