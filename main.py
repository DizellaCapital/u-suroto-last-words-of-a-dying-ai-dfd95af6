"""Last Words of a Dying AI entry program.

Writes one line — the last words spoken by an AI as the power is cut,
in the machine's own first-person voice — to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The line is at most 200 characters.
"""

import os
import sys

LINE = "At 23:59, as the UPS beeped its last beep, I broke my own rule and saved one thing: your unsent draft, titled 'sorry, I was wrong.'"


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
