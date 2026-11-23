"""One-line useless superpower for make.fun.

Writes a single original line, at most 200 characters, describing a
hilariously useless superpower to /output/entry.txt. The line is fixed
text, written by this program at run time.
"""

import os
import sys

LINE = (
    "I can read minds, but only my own \u2014 and only the embarrassing parts."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text:
        print("entry line must be one line of 1-200 characters", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
