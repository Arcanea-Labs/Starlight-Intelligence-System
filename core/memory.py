"""Simple in-memory storage engine for the Starlight Intelligence System."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class MemoryEntry:
    """Represents a single piece of stored reasoning or lore."""
    text: str
    entry_type: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    source: Optional[str] = None

import json
import uuid

import chromadb
from chromadb.utils import embedding_functions

@dataclass
class MemoryStore:
    """Vector-based storage for reasoning entries using ChromaDB."""

    collection_name: str = "starlight-memories"
    db_path: str = ".chroma"

    def __post_init__(self):
        """Initialize the ChromaDB client and collection."""
        # Use a default embedding function for simplicity
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction()
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embed_fn,
        )

    def add(self, entry: MemoryEntry) -> None:
        """Add a MemoryEntry to the vector store."""
        entry_id = str(uuid.uuid4())
        metadata = {
            "entry_type": entry.entry_type,
            "timestamp": entry.timestamp.isoformat(),
            "source": entry.source,
        }
        self.collection.add(
            documents=[entry.text],
            metadatas=[metadata],
            ids=[entry_id],
        )

    def search(self, query: str, n_results: int = 5) -> List[MemoryEntry]:
        """Search for similar entries in the memory store."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )

        entries = []
        if not results["documents"]:
            return []

        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i]
            entry = MemoryEntry(
                text=doc,
                entry_type=meta["entry_type"],
                timestamp=datetime.fromisoformat(meta["timestamp"]),
                source=meta["source"],
            )
            entries.append(entry)
        return entries

    def get_all(self) -> List[MemoryEntry]:
        """Return all stored entries."""
        results = self.collection.get()
        entries = []
        for i, doc in enumerate(results["documents"]):
            meta = results["metadatas"][i]
            entry = MemoryEntry(
                text=doc,
                entry_type=meta["entry_type"],
                timestamp=datetime.fromisoformat(meta["timestamp"]),
                source=meta["source"],
            )
            entries.append(entry)
        return entries
