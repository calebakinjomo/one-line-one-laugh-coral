"""One Line, One Laugh — make.fun bounty u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
The line is the whole entry: a setup with a turn the reader does not see coming.
"""

import os

LINE = (
    "I told my smart fridge I'm on a diet. "
    "It now judges me in Celsius and hides the chocolate behind the vegetables."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
