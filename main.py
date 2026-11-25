#!/usr/bin/env python3
"""Snooze Button Roast — u-carbon-forge-snooze-button-roast-14cbafc6.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt (UTF-8, no network at run time).
Python 3.13 standard library only.
"""

import os

ENTRY = "My alarm rings at 6 AM on Saturday \u2014 the snooze button is its witness protection program."


def main() -> None:
    # Gate: the entry must be exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify what was written matches the gate too.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output differs from entry"
    assert written.count("\n") == 1, "output must be exactly one line"


if __name__ == "__main__":
    main()
