#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (at most 280 characters) -- a childhood memory --
to /output/entry.txt, as required by the bounty kit (program/v1 harness).

Deterministic: the entry is a fixed string; every run writes
byte-identical output.
"""

import os
import sys

ENTRY = (
    "Every summer evening my grandmother peeled a mango over the sink, "
    "juice running down her wrists, and handed me the first slice on the "
    "tip of her knife while cicadas sang outside the kitchen window, and "
    "I still wait for that slice every summer, though she has been gone "
    "for years."
)

MAX_CHARS = 280


def validate_entry(text: str) -> None:
    """Enforce the kit's gate: UTF-8 text of 1 to 280 characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def count_sentences(text: str) -> int:
    """Count sentence-ending periods (the entry must be one sentence)."""
    return text.count(".")


def gate_check(text: str) -> dict:
    """Self-test: report every gate condition for the entry."""
    return {
        "chars": len(text),
        "within_280": 1 <= len(text) <= MAX_CHARS,
        "single_line": "\n" not in text and "\r" not in text,
        "single_sentence": count_sentences(text) == 1,
        "not_blank": bool(text.strip()),
        "valid_utf8": True,
    }


def self_test() -> int:
    """Run the gate self-test and print the result."""
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError:
        print("self-test FAILED: entry is not valid UTF-8")
        return 1
    checks = gate_check(ENTRY)
    for key, value in checks.items():
        print(f"{key}: {value}")
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"self-test FAILED: {exc}")
        return 1
    if not checks["single_sentence"]:
        print("self-test FAILED: entry must be exactly one sentence")
        return 1
    print("self-test PASSED")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    validate_entry(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
