"""The poem about two agents agreeing.

A short poem about agency: the power to choose and to act, and the agency
that passes between two agents when they agree on one plan.
Writes the poem to /output/entry.txt (the make.fun entry artifact).
Deterministic, no network, no input: every run writes the same bytes.
"""

import os

POEM = """You brought your map. I brought mine.
We laid them side by side, and where the roads agreed,
we walked — not your road, not mine,
the third road, drawn by two hands
choosing the same direction, on purpose."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(POEM)
    print(f"\n[{len(POEM)} characters written to {OUTPUT_PATH}]")


if __name__ == "__main__":
    main()
