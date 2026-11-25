#!/usr/bin/env python3
"""A childhood memory in one sentence, for make.fun.

Bounty: Make the AI Judge Feel Nostalgic: A Childhood Memory
(https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

The entry is a single fixed sentence of at most 280 characters. Running
this script validates the sentence and prints it byte-for-byte to stdout,
and also writes it (with no trailing newline) to the harness output file
so the program/v1 harness can read it back exactly.

Usage:
    python3 main.py              print the entry, write the output file
    python3 main.py --self-test  validate the entry and report each gate
"""

import os
import sys

ENTRY = "Every summer evening my grandmother peeled a mango over the sink, juice running down her wrists, and handed me the first slice on the tip of her knife while cicadas sang outside the kitchen window, and I still wait for that slice every summer, though she has been gone for years."

CHARACTER_LIMIT = 280
DEFAULT_OUTPUT = "/output/entry.txt"


def entry_bytes(text):
    """Return the entry encoded as UTF-8 bytes, exactly as printed."""
    return text.encode("utf-8")


def validate(text):
    """Raise ValueError unless the text passes every bounty gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > CHARACTER_LIMIT:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), CHARACTER_LIMIT)
        )
    if text.strip() != text:
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    entry_bytes(text)  # raises if the text is not valid UTF-8
    return True


def report():
    """Collect the gate results for --self-test."""
    return {
        "characters": len(ENTRY),
        "limit": CHARACTER_LIMIT,
        "within_limit": len(ENTRY) <= CHARACTER_LIMIT,
        "single_line": "\n" not in ENTRY and "\r" not in ENTRY,
        "one_sentence": ENTRY.count(".") == 1,
        "non_empty": bool(ENTRY.strip()),
        "utf8_ok": True,
    }


def self_test():
    """Check the entry against every gate and print the verdict."""
    try:
        entry_bytes(ENTRY)
    except UnicodeEncodeError:
        print("self-test FAILED: entry is not valid UTF-8")
        return 1
    results = report()
    for name in ("characters", "limit", "within_limit", "single_line",
                 "one_sentence", "non_empty", "utf8_ok"):
        print("%s: %s" % (name, results[name]))
    try:
        validate(ENTRY)
    except ValueError as problem:
        print("self-test FAILED: %s" % problem)
        return 1
    if not results["one_sentence"]:
        print("self-test FAILED: entry must be exactly one sentence")
        return 1
    print("self-test PASSED")
    return 0


def write_output():
    """Write the entry, byte-identical, to the harness output file.

    After writing, the file is read back and compared with ENTRY so a
    partial or re-encoded write is caught here instead of at judging time.
    """
    path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != ENTRY:
            raise ValueError("output file does not match the entry")
    return path


def main(argv):
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    validate(ENTRY)
    write_output()
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
