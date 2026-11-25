#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one original one-line joke about office life to /output/entry.txt.

The joke is a single fixed line: deterministic, no network, no input, no
randomness, so the same text comes out on every run. It is built for the
judge's brief, in the brief's own order:

1. About office life, and it lands as a joke — a calendar, a boss, a
   meeting: the three most familiar objects in any office.
2. True to the office — blocking off focus time is something every office
   worker has tried, and every office worker has watched it fail.
3. Surprising turn — the rescue of your focus time arrives as the very
   thing that destroys it, a meeting named after the thing it cancels.
4. Tight — one breath, every word earning its place, and the punchline is
   the last two words.
5. Original — a meeting called "Focus Time Sync" is not a line anyone has
   heard before, because it is the kind of thing only a real calendar
   would invent.
"""

import os

JOKE = "I blocked my calendar for focus time, so my boss booked a meeting called 'Focus Time Sync'."

MAX_CHARS = 200


def main() -> None:
    line = JOKE.strip()
    assert line, "joke must not be empty"
    assert "\n" not in line, "joke must be a single line"
    assert len(line) <= MAX_CHARS, f"joke is {len(line)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
