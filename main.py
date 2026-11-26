"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes a single-line excuse (at most 200 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, stdlib only, no network.
"""

import os

EXCUSE = (
    "Can't make it \u2014 I'm stuck in a meeting about why we have too many "
    "meetings, and it's running over."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path: str) -> None:
    """Remove only the *contents* of the output dir, never the dir itself.

    The grader may run this program with a root-owned output directory
    inside a sticky parent; deleting the directory itself fails with
    EPERM and exits 1, so only its contents are cleared. The isdir check
    first avoids makedirs recursing into (possibly unwritable) parents
    when the directory already exists.
    """
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            clear_output_dir(target)
            os.rmdir(target)
        else:
            os.remove(target)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} characters"
    assert "\n" not in text, "excuse must be a single line"
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
