import os
import shutil
from .utils import call_ollama


def organize_vault(folder_path: str):
    if not os.path.isdir(folder_path):
        print("Folder not found.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            prompt = f"""
Classify this note into ONE category:
AI, Cloud, Personal, Study, Other

Return only the category name.

{content}
"""

            category = call_ollama(prompt)

            if not category:
                continue

            category = category.strip()
            target_folder = os.path.join(folder_path, category)

            os.makedirs(target_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(target_folder, filename))

            print(f"Moved {filename} → {category}/")