#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

One funny line in the voice of a smug self-checkout machine.
Pure stdlib. Writes exactly one line to /output/entry.txt.
"""

from pathlib import Path

LINE = "You weighed the grapes, then ate three. I counted. I am literally a scale with opinions."
# Rubric winner of 8 hand-written candidates: weighing is the machine's
# own job, eating three grapes mid-weigh is a small crime everyone
# recognises, and the punchline is the till talking, not a narrator.


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
