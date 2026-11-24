#!/usr/bin/env python3
"""The Dog Ate My Homework — writes one excuse to /output/entry.txt."""

ENTRY = "It was sitting on the floor, unguarded, smelling of pencil and fear \u2014 I didn't eat your homework, I conducted a quality inspection and it failed."


def main():
    import os
    # Gate: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) < 200, "entry must be under 200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
