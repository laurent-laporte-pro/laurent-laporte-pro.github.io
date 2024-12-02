import csv
import datetime
import re
from pathlib import Path

from laurent_laporte_pro_github_io import PROJECT_DIR


class ParseError(Exception):
    def __init__(self, path: Path, line_no: int, message: str, line: str):
        err_msg = f"Error in '{path.relative_to(PROJECT_DIR)}' at line {line_no}: {message}\n=> {line}"
        super().__init__(err_msg)


def convert_to_record(level: int, title: str, from_date: datetime.date, to_date: datetime.date):
    duration = (to_date - from_date).days / 365
    years, months = divmod(duration * 12, 12)
    years_str = f"{int(years)} years" if years > 1 else "1 year"
    months_str = f"{int(months)} months" if months > 1 else ("1 month" if months else "")
    duration_str = f"{years_str} {months_str}".strip()
    return {
        "level": str(level),
        "title": title,
        "from_date": from_date.isoformat(),
        "to_date": to_date.isoformat(),
        "duration": duration_str,
    }


def extract_position_dates(md_path: Path, csv_path: Path) -> None:
    level: int
    title: str
    from_date: datetime.date
    to_date: datetime.date

    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open(mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["level", "from_date", "to_date", "duration", "title"])
        writer.writeheader()

        with md_path.open(mode="r", encoding="utf-8") as md_file:
            for no, line in enumerate(md_file, 1):
                line = line.strip()

                try:
                    if line.startswith("#"):
                        level = line.count("#")
                        title = re.sub(r"#+\s", "", line)

                    elif line.startswith("⇨") and "<input" in line:
                        from_date = parse_input_date(line)

                    elif "<input" in line:
                        to_date = parse_input_date(line)
                        record = convert_to_record(level, title, from_date, to_date)
                        writer.writerow(record)

                except ValueError as exc:
                    raise ParseError(md_path, no, str(exc), line) from exc


def parse_input_date(line: str) -> datetime.date:
    mo = re.search(r'<input type="date" value="(\d+)-(\d+)-(\d+)" readonly>', line)
    if mo is None:
        raise ValueError("Invalid date input")
    year, month, day = mo.groups()
    date = datetime.date(int(year), int(month), int(day))
    return date


def main():
    for lang in ["fr", "en", "de"]:
        src_path = PROJECT_DIR / f"docs/{lang}/index.md"
        dst_path = PROJECT_DIR / f"data/positions.{lang}.csv"
        extract_position_dates(src_path, dst_path)


if __name__ == '__main__':
    main()
