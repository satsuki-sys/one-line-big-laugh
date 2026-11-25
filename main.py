#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single hilarious line, 200 characters or fewer, to
/output/entry.txt. The line stands entirely on its own: no title,
no setup, no explanation around it.
"""

import os

ENTRY = (
    "My Roomba filed for divorce after cleaning the same spaghetti off "
    "my floor three nights in a row, and the judge ruled in its favor, "
    "noting it was the only one in the marriage who ever finished a job."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert line.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
