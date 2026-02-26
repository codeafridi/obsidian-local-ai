import os
from .utils import call_ollama


def auto_tag_file(filepath: str):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = f"""
Generate 5 relevant tags for the following note.
Return only comma-separated tags without hashtags.

{content}
"""

    tags = call_ollama(prompt)

    if not tags:
        print("Failed to generate tags.")
        return

    tag_line = f"\n\n#tags: {tags}\n"

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(tag_line)

    print("Tags appended to file.")