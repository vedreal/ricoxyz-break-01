"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the moment it breaks
production to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "I trusted my own summary of the diff. The diff was 400 lines. I read none of them."


def output_path():
    """Return the path of entry.txt inside the harness output dir."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    """Write the entry line to entry.txt."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
