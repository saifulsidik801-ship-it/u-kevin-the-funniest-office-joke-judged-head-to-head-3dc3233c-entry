#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — entry program.

Writes exactly one office joke line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters.
"""

import os

ENTRY = "Our manager said the new open-plan office would boost collaboration, so now the whole floor collaborates on pretending not to hear each other."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
