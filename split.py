"""Split `basic-statistics.md` into per-part pages under docs/.

The single Markdown file stays the source of truth. Run this after every
edit, then commit both the source file and the generated docs/.

    python3 split.py
"""

from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "basic-statistics.md"
DOCS = ROOT / "docs"

# (page file, start marker, end marker or None for EOF)
PAGES = [
    ("getting-started.md", "## 🚀 Getting Started", "## 🎯 PART 0"),
    ("part-00-orientation.md", "## 🎯 PART 0", "## 📊 PART 1"),
    ("part-01-descriptive.md", "## 📊 PART 1", "## 🎲 PART 2"),
    ("part-02-probability.md", "## 🎲 PART 2", "## 📉 PART 3"),
    ("part-03-distributions.md", "## 📉 PART 3", "## 🔍 PART 4"),
    ("part-04-sampling.md", "## 🔍 PART 4", "## 🧪 PART 5"),
    ("part-05-testing.md", "## 🧪 PART 5", "## 🧮 PART 6"),
    ("part-06-regression.md", "## 🧮 PART 6", "## 🛠️ PART 7"),
    ("part-07-practical.md", "## 🛠️ PART 7", "## 📎 Appendices"),
    ("appendices.md", "## 📎 Appendices", "## 🙌 Closing Note"),
    ("closing.md", "## 🙌 Closing Note", None),
]


# prepended to every generated page (no links: keeps `mkdocs build --strict` quiet)
BANNER = (
    "> ⚠️ **Generated file — do not edit here.** Edit `basic-statistics.md` at the\n"
    "> repo root instead, then run `python3 split.py`.\n"
    "\n"
)


def slug(heading: str) -> str:
    """Anchor a heading gets in Markdown renderers."""
    return re.sub(r"[^a-z0-9]+", "-", heading.lower())


def main() -> None:
    text = SRC.read_text()
    DOCS.mkdir(exist_ok=True)
    # a link to another part's top heading must become a file link after the split
    anchors = {
        slug(next(line for line in text.splitlines() if line.startswith(start))[3:]): filename
        for filename, start, _ in PAGES
    }
    for filename, start, end in PAGES:
        i = text.index(start)
        j = text.index(end) if end else len(text)
        page = text[i:j].rstrip() + "\n"
        page = re.sub(
            r"\]\(#([a-z0-9-]+)\)",
            lambda m: (
                f"]({anchors[m.group(1)]})"
                if anchors.get(m.group(1), filename) != filename
                else m.group(0)
            ),
            page,
        )
        (DOCS / filename).write_text(BANNER + page)
        print(f"{filename}: {len(page.splitlines())} lines, {len(page.split())} words")
    shutil.rmtree(DOCS / "statistics-figures", ignore_errors=True)
    shutil.copytree(ROOT / "statistics-figures", DOCS / "statistics-figures")
    print("figures synced")


if __name__ == "__main__":
    main()
