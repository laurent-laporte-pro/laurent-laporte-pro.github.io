"""
Change the postal address in the markdown files of the website.
"""
import re
from pathlib import Path

from laurent_laporte_pro_github_io import PROJECT_DIR

NEW_ADDRESSES = {
    "fr": "3 rue des lilas, 53440 La Bazoge-Montpinçon",
    "en": "3 rue des lilas, 53440 La Bazoge-Montpinçon, France",
    "de": "3 rue des lilas, 53440 La Bazoge-Montpinçon, Frankreich",
}


def change_address(src_path: Path, dst_path: Path, *, lang: str) -> None:
    content = src_path.read_text()
    new_address = NEW_ADDRESSES[lang]
    content = re.sub(r"(\*\*(?:Address|Adresse)\s*:\*\*\s+)(.+)", f"\\g<1>{new_address}", content, flags=re.IGNORECASE)
    dst_path.write_text(content)


def main():
    for lang in ["fr", "en", "de"]:
        src_path = PROJECT_DIR / f"docs/{lang}/index.md"
        dst_path = PROJECT_DIR / f"docs/{lang}/index.md"
        change_address(src_path, dst_path, lang=lang)


if __name__ == '__main__':
    main()
