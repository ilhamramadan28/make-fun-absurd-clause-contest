#!/usr/bin/env python3
"""The Absurd Clause Contest — one deadpan ToS clause, max 200 chars.

Writes a single original English sentence, phrased as a clause buried
deep inside a terms-of-service agreement: legal boilerplate on the
surface, absurd the moment you actually read it.
"""
import os

ENTRY = (
    "Section 12.3: the User grants the Company a perpetual, "
    "royalty-free license to the User's dreams, including the right "
    "to sublicense any recurring nightmare to the highest bidder."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip() == text and len(text.splitlines()) == 1
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
