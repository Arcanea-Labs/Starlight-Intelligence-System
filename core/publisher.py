"""Publishes session traces to Markdown files."""

from __future__ import annotations

import os
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .session import Session

class Publisher:
    """Formats and saves session traces as Starlight Notes."""

    def __init__(self, output_dir: str = "starlight-notes"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def publish_session(self, session: Session) -> str:
        """
        Generates a Markdown report from a session and saves it to a file.

        Returns the path to the generated file.
        """
        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
        filename = f"note-{timestamp}.md"
        filepath = os.path.join(self.output_dir, filename)

        entries = session.trace()

        markdown_lines = [
            f"# Starlight Note: {timestamp}",
            "\n",
            "## Session Trace",
            "\n",
        ]

        for entry in entries:
            markdown_lines.append(f"**[{entry.entry_type.upper()}]** - {entry.timestamp.isoformat()} - (Source: {entry.source or 'Unknown'})")
            markdown_lines.append("> " + entry.text.replace("\n", "\n> "))
            markdown_lines.append("\n")

        markdown_content = "\n".join(markdown_lines)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        return filepath
