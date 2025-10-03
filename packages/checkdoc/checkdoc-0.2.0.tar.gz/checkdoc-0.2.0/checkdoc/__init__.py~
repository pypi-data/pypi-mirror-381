"""Scan a word document for key phrases."""

from __future__ import annotations

# Python imports
import argparse
from typing import Any

# Module imports
from docx import Document


def find_phrases_in_docx(file_path: str, phrases: list[str]) -> list[str]:
    """Find phrases in a docx file."""
    doc = Document(file_path)
    matches = []

    def scan_para(obj: Any) -> list[str]:
        matches = []
        for para in obj.paragraphs:
            text = para.text.strip()
            if any(phrase.lower() in text.lower() for phrase in phrases):
                matches.append(text)
        return matches

    matches += scan_para(doc)

    for tab in doc.tables:
        for row in tab.rows:
            for cell in row.cells:
                matches += scan_para(cell)

    return matches

def main() -> None:
    """Check the word document from the CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Scan a Word document for key phrases.",
    )
    parser.add_argument("file", help="Path to the .docx file")
    parser.add_argument("phrases", nargs="+", help="Key phrases to search for")
    args = parser.parse_args()

    results = find_phrases_in_docx(args.file, args.phrases)

    for line in results:
        print(line)     # noqa: T201

if __name__ == "__main__":
    main()
