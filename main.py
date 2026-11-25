#!/usr/bin/env python3
"""One Line, One Laugh — entry writer.

Writes a single funny line to /output/entry.txt. Fully deterministic and
offline: the line is a constant, there is no randomness, no network access,
no clock or environment reading, and no path-dependent output.
"""

import os

LINE = (
    "I taught my dog to fetch my slippers; he now delivers one slipper "
    "and an itemised invoice for emotional labour."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate mirror: the entry must be 1-200 characters of non-blank text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
