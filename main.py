#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line -- the excuse a dog gives after being caught eating the
homework, in the dog's own voice -- to /output/entry.txt.

Standard library only, deterministic, no network, no trailing newline.
"""

import os

ENTRY = "I didn't eat your homework, I graded it: C-minus. The margins were delicious."

# The sealed gate needs 1-200 chars, a single line, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
