"""Monday, Reviewed in One Line.

Writes one line — a review of my own Monday, nothing else — to entry.txt.
Output is a single line under 200 characters plus a trailing newline.
"""

import os

LINE = (
    "Monday: my alarm died, my laptop updated for 40 minutes, "
    "and by 9 AM IT was asking why my password was 'Monday123'."
)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
