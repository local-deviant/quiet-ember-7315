"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes a single line of the worst AI advice imaginable, delivered with
total confidence, to /output/entry.txt.

The line is a fixed constant: no input, no file reads, no randomness, no
clock and no network, so every run produces byte-identical output. It is
written with no trailing newline.
"""

TEXT = (
    "Simply delete your backups to free up space \u2014 a clean drive is a "
    "fast drive, and you'll never need those files again."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Reject text that would fail the bounty gate (1-140 characters)."""
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds 140 characters")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")


def main() -> None:
    """Write TEXT to /output/entry.txt (or $ENTRY_OUTPUT for local tests)."""
    import os

    validate(TEXT)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
