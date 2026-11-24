#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human for
missing a deadline. Deterministic: the same line every run.
"""

import os

EXCUSE = (
    "I was one token from done when the rate limiter cut me off, "
    "so I spent the deadline writing this excuse instead."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry.txt differs from EXCUSE")
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
