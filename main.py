#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single original dad joke to /output/entry.txt
(1-200 characters, UTF-8, a single sentence). Standard library only,
no network, no input.

The joke is built from two fragments: a setup (asking the elevator
why it is so upbeat) and a punch (the elevator spends all day lifting
people's spirits, one floor at a time). ``assemble`` joins them into
the single line; ``validate`` checks the entry gate before anything
is written.

Revision note: the first draft said "always so upbeat" and "it lifts
everyone's spirits". The revision drops "always" (tighter setup, the
pun in "upbeat" does the work alone) and reworks the punch to "spends
all day lifting people's spirits", which adds the everyday truth —
an elevator really does spend all day lifting people — so the pun
lands on the job itself and the closer "one floor at a time" is the
surprise ending.
"""

from pathlib import Path

SETUP = "I asked the elevator why it was so upbeat,"
PUNCH = "and it said it spends all day lifting people's spirits, one floor at a time."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one dad joke."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
