#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a sick-day
excuse built on a fresh angle — the immune system as a software update
that keeps restarting its owner every twenty minutes since 3 a.m.
"""

import os

ENTRY_TEXT = (
    "Hi, calling in sick today: my immune system pushed a software update "
    "at 3 a.m. and it's been restarting me every twenty minutes since."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
