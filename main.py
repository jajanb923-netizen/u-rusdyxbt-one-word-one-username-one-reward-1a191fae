#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- one word, nothing else --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Entry: jajanb923-netizen (17 characters, no @, no spaces, no padding).
The handle itself is the entry; the judge compares usernames two at a
time on funniness and memorability, so the program's only job is to
emit the genuine handle exactly, deterministically, every run.

Python 3.13 standard library only. No network, no randomness, no
environment secrets. Deterministic: same bytes on every run.
"""

import os
import sys

# The entrant's own make.fun username, exactly as registered.
USERNAME = "jajanb923-netizen"

# Sealed gate limits from RULES.txt: UTF-8 text of 1 to 30 characters,
# not only white space; a single word with no padding or gloss.
MAX_CHARS = 30
MIN_CHARS = 1


def gate_errors(text: str) -> list:
    """Return every gate violation for a candidate entry text."""
    errors = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        errors.append(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        errors.append("entry must not be only white space")
    if any(ch.isspace() for ch in text):
        errors.append("entry must be a single word (no white space)")
    if text.startswith("@") or text.endswith("@"):
        errors.append("entry must be the bare handle, no @ prefix")
    if text != USERNAME:
        errors.append("entry must be the entrant's own username")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry must be valid UTF-8")
    else:
        if len(encoded) != len(text):
            errors.append("entry must be plain ASCII handle bytes")
    return errors


def write_entry(text: str, out_dir: str) -> str:
    """Write the checked entry and verify the bytes read back."""
    problems = gate_errors(text)
    if problems:
        raise SystemExit("gate check failed: " + "; ".join(problems))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt is not the handle")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(USERNAME, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
