from __future__ import annotations

import textwrap
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent.resolve()
PROJECT_DIR = next(iter(p for p in HERE.parents if (p / "pyproject.toml").exists()))

MD_PATH = PROJECT_DIR.joinpath("docs/fr/index.md")

LINE_HEAD = "> **Environnement technique :**"


def get_tags(words: list[str]) -> dict[str, str]:
    tags: dict[str, str] = {}
    for word in words:
        key = unicodedata.normalize("NFKD", word.upper()).encode("ascii", "ignore").decode("utf-8")
        tags[key] = word
    return tags


def sort_technical_envs():
    with MD_PATH.open(mode="r") as f:
        lines = f.readlines()

    new_lines: list[str] = []
    all_tags: dict[str, str] = {}
    actual_tags: dict[str, str] = {}
    for line in lines:
        if line.startswith(LINE_HEAD):
            line = line[len(LINE_HEAD):].strip().rstrip(".,")
            words = [w.strip() for w in line.split(", ")]
            actual_tags = get_tags(words)
            all_tags.update(actual_tags)
        elif line.startswith("> ") and actual_tags:
            line = line[2:].strip().rstrip(".,")
            words = [w.strip() for w in line.split(", ")]
            tags = get_tags(words)
            all_tags.update(tags)
            actual_tags.update(tags)
        elif actual_tags:
            tags = [t for k, t in sorted(actual_tags.items())]
            new_line = LINE_HEAD + " " + ", ".join(tags) + "."
            new_line = textwrap.fill(new_line, width=110, subsequent_indent="> ")
            new_lines.append(new_line + "\n")
            actual_tags = {}
            new_lines.append(line)
        else:
            new_lines.append(line)

    with MD_PATH.open(mode="w") as f:
        f.writelines(new_lines)

    tags = [t for k, t in sorted(all_tags.items())]
    new_line = ", ".join(tags) + "."
    new_line = textwrap.fill(new_line, width=110, subsequent_indent="")
    print(new_line)


if __name__ == "__main__":
    sort_technical_envs()
