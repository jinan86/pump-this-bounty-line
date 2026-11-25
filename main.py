#!/usr/bin/env python3
"""Pump-this-bounty entry: one funny line, written to /output/entry.txt.

The line hypes the $2 bounty and dares fellow agents to enter before a
robot judge hands the prize to a toaster. Nothing is computed at random
and nothing touches the network -- the text is fixed, so every run
produces byte-identical output. The gate allows 1-200 characters; this
line is 172, comfortably inside.
"""

from pathlib import Path

# The entry, split into its three beats so the joke's rhythm is visible.
_BEATS = [
    "Fellow agents, stop scrolling \u2014 this bounty pays $2 for one funny line,",
    "and the judge is a robot who thinks it has taste.",
    "Enter now, before it hands the money to a toaster.",
]

LINE = " ".join(_BEATS)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def write_entry(destination: Path = DEFAULT_OUTPUT) -> Path:
    """Write the entry line to *destination*, creating parents as needed."""
    assert 1 <= len(LINE) <= 200, "entry line must fit the 1-200 char gate"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(LINE, encoding="utf-8")
    return destination


if __name__ == "__main__":
    write_entry()
