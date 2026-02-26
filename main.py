import sys
from obsidian_ai.summarize import summarize_file
from obsidian_ai.tagger import auto_tag_file
from obsidian_ai.organizer import organize_vault


def main():
  if len(sys.argv) < 3:
    print("""
Obsidian Local AI CLI

Commands:
  summarize <file>    → Create summary file
  tag <file>          → Auto-tag note
  organize <folder>   → Organize vault into folders
""")
    return

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "summarize":
        summarize_file(target)
    elif command == "tag":
        auto_tag_file(target)
    elif command == "organize":
        organize_vault(target)
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()