#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short, calm passage to /output/entry.txt: the night sky
over an empty sea, the first light after a long dark. Awe through
vastness and stillness, not spectacle. Deterministic, stdlib only,
no network.
"""

import os

TEXT = (
    "The night sky over an empty sea. No lights, no shore, only water "
    "holding the dark and the dark holding stars. You stand small at its "
    "edge, and the quiet asks nothing of you. Far above, a first "
    "light gathers, slow and pale, and the sky breathes. There is room "
    "here for all of it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
