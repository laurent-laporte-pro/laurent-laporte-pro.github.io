"""
Réordonner les expériences concernant Luminess dans l'ordre chronologique inverse.
"""
from pathlib import Path

from laurent_laporte_pro_github_io import PROJECT_DIR


def update_luminess_order(src_path: Path, dst_path: Path) -> None:
    """
    Sort Luminess sections in reverse chronological order (most recent first).

    We assume that the Luminess sections are sorted in chronological order in the markdown file.

    :param src_path: Full path to the markdown file to update.
    :param dst_path: Full path to the new markdown file.
    """
    content = src_path.read_text()
    lines = content.splitlines(keepends=True)
    new_lines = []

    # Lecture des lignes jusqu'à la section contenant le mot "Luminess"
    in_luminess = False
    luminess_sections = []

    for line in lines:
        if in_luminess:
            if luminess_sections:
                if line.startswith("#### "):
                    # Nouvelle section
                    luminess_sections.append([line])
                elif line.startswith("### "):
                    # Fin de la section "Luminess"
                    in_luminess = False
                    for section in reversed(luminess_sections):
                        new_lines.extend(section)
                    luminess_sections[:] = []
                    new_lines.append(line)
                else:
                    luminess_sections[-1].append(line)
            else:
                if line.startswith("#### "):
                    luminess_sections.append([line])
                else:
                    new_lines.append(line)

        elif "Luminess" in line:
            in_luminess = True
            new_lines.append(line)
        else:
            new_lines.append(line)

    # Écriture du fichier
    dst_path.write_text("".join(new_lines))


def main():
    for lang in ["fr", "en", "de"]:
        src_path = PROJECT_DIR / f"docs/{lang}/index.md"
        dst_path = PROJECT_DIR / f"docs/{lang}/index.new.md"
        update_luminess_order(src_path, dst_path)


if __name__ == '__main__':
    main()
