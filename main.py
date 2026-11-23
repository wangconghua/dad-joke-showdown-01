#!/usr/bin/env python3
"""Write one dad joke, at most 200 characters.

The joke is a fixed text: a dad explains what a kleptomaniac is to his
son, and the punchline turns on "takes things literally". The pun lands
on the first read: a kleptomaniac takes things, and "takes literally"
is the turn. The program
checks the text fits the competition's 1-200 character window, then
writes it to /output/entry.txt as UTF-8.
"""

import os

JOKE = (
    "My son asked me what a kleptomaniac is. "
    "I said, 'Someone who takes things literally.'"
)


def main() -> None:
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
