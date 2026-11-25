"""The Absurd Clause Contest — make.fun entry.

Writes one original absurd terms-of-service clause to /output/entry.txt.
Pure standard library only; deterministic.
"""

import os

CLAUSE = (
    "You agree that your left shoe remains the property of the Company "
    "and may be repossessed at any time by a representative wearing the "
    "right shoe."
)


def main() -> None:
    text = CLAUSE.strip()
    assert text, "clause must not be empty"
    assert text == text.strip(), "clause must not have surrounding whitespace"
    assert "\n" not in text and "\r" not in text, "clause must be one line"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"clause must be 1-200 chars, got {len(text)}"
    assert text.strip(), "clause must not be whitespace-only"
    # One sentence: exactly one sentence-terminating period, at the end.
    assert text.endswith(".") and text.count(".") == 1, "clause must be one sentence"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be byte-identical
    # to the clause we validated above (no added newline, no re-encoding).
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == encoded, "entry.txt on disk differs from validated clause"
    assert on_disk.decode("utf-8") == text
    print(text)
    print(f"[{len(text)} chars, {len(encoded)} bytes]")


if __name__ == "__main__":
    main()
