import os

# One letter, A for coffee or B for tea. Coffee is the livelier,
# more vivid stance: the first cup of the day, not a polite infusion.
CHOICES = {"coffee": "A", "tea": "B"}
LETTER = CHOICES["coffee"]


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
