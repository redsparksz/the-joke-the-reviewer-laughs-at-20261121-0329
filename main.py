"""Write one joke about working beside AI coding agents to /output/entry.txt.

Stdlib only, no network, deterministic: every run writes the same bytes.
"""

import os

JOKE = (
    "My AI coding agent is the best junior dev I've ever had: it never sleeps, "
    "never complains, and confidently ships bugs at a speed I could only dream of."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-280 Unicode code points of non-whitespace text.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
