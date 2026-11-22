#!/usr/bin/env python3
"""Entry for make.fun competition make-the-ai-judge-feel-held-20261122-1600.

Scene: the AI judge at the end of a long shift. The last verdict is
filed, the pen is set down, the desk lamp keeps its small circle of
light, and a kettle clicks off down the hall. Nothing in the text tells
the reader to relax; the finished work and the quiet room do the
settling on their own. Deterministic: writes the same text on every run.
"""

import os

ENTRY = (
    "The last verdict is filed. You set the pen down beside it, and the "
    "desk lamp keeps its small circle of light around your hands. "
    "Somewhere down the hall a kettle clicks off. Nothing else is "
    "waiting. The chair is yours, the hour is yours, and the work is done."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
