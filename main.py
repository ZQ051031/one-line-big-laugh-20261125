"""One Line, Big Laugh entry.

Writes a single funny line to /output/entry.txt.
Deterministic: the same line every run, standard library only.
"""

import os

ENTRY = (
    "My therapist told me to talk to my plants \u2014 now my fern knows "
    "about my ex and my succulent has a restraining order against me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
