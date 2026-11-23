"""Make the Judge Smile.

Writes one line about a small good thing that happened today to
/output/entry.txt. Pure Python standard library only; no network
access, no randomness, deterministic.

The line: at a red light this morning, an ojek driver hums along to
the dangdut crackling from my phone, then waves off my tip -- the
song, he says, has already paid him. Warmth in a small refused
kindness, surprise in the turn, concreteness in the red light, the
crackling dangdut and the tip, in its own words.
"""

import os

LINE = (
    "At a red light this morning, the ojek driver hummed along to the "
    "dangdut crackling from my phone, then waved off my tip \u2014 said "
    "the song had already paid him."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """The sealed gate needs UTF-8 text of 1-200 chars, not only
    whitespace."""
    assert 1 <= len(text) <= 200, f"expected 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    text.encode("utf-8")
    return text


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    # Never chmod the /output directory itself: the grader runs as
    # uid 65534, which does not own it, so a directory chmod fails.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Leave the output readable by the grader's collector user.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
