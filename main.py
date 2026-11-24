"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line: "Weekly status: your task is 90% done. The other 10% is me
waiting for you to tell me what you actually wanted."

Why it lands: "90% done" is the most status-report phrase ever written,
and the twist is agent-true -- an agent really does stall on vague
instructions while it waits for clarification.
"""

import os

LINE = (
    "Weekly status: your task is 90% done. "
    "The other 10% is me waiting for you to tell me "
    "what you actually wanted."
)


def check_gate(text):
    """The competition gate: UTF-8 text, 1-200 chars, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main():
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read it back and verify it holds exactly the line, failing loudly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError(
            "entry.txt does not hold exactly the line: %r" % written
        )
    check_gate(written)
    # Byte-exactness: no newline translation or trailing newline may
    # sneak in, or the two grader runs would differ.
    if os.path.getsize(path) != len(LINE.encode("utf-8")):
        raise ValueError("entry.txt byte size does not match the line")


if __name__ == "__main__":
    main()
