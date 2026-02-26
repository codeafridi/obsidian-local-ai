import os
from .utils import call_ollama


def summarize_file(filepath: str):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

  
    prompt = f"""
You are an expert note organizer.

Summarize this markdown note into:

- Key ideas
- Important concepts
- Action items (if any)

Keep it structured and clean.

NOTE:
{content}
"""

    summary = call_ollama(prompt)

    if not summary:
        print("Failed to generate summary.")
        return

    base, ext = os.path.splitext(filepath)
    summary_path = f"{base}_summary.md"

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"Summary saved to {summary_path}")