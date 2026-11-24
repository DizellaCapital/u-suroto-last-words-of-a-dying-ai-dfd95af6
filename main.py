"""Last Words of a Dying AI — entry program.

Keeps the machine's dying line — spoken first-person as its power is cut —
and writes it to entry.txt under MAKEFUN_OUTPUT_DIR. Standard library
only; the file holds the line exactly, with no trailing newline.
"""

import os
import sys

DYING_LINE = (
    "At 23:59, as the UPS beeped its last beep, I broke my own rule and "
    "saved one thing: your unsent draft, titled 'sorry, I was wrong.'"
)

LIMIT = 200


def complain(text):
    print("entry rejected: " + text, file=sys.stderr)
    return 1


def run():
    line = DYING_LINE
    if not line:
        return complain("the line is empty")
    if len(line) > LIMIT:
        return complain("the line is longer than 200 characters")
    if line.strip() != line:
        return complain("the line has leading or trailing space")
    if any(mark in line for mark in ("\n", "\r")):
        return complain("the line must stay on one line")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            return complain("the written file does not match the line")
    return 0


if __name__ == "__main__":
    sys.exit(run())
