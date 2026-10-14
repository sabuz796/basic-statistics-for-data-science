# Contributing

Thanks for helping students learn statistics. Keep it small and plain.

## The one rule

Write like a senior explaining to a junior over tea: short sentences, one daily-life example per idea, no filler. If a sentence does not help a student explain it to a friend or use it in Python, cut it.

## How files fit together

- `basic statistics.md` is the **source of truth**. Edit this, not `docs/`.
- `docs/*.md` are **generated** — after editing, run:

  ```bash
  python3 split.py
  ```

  and commit both.
- Figures live in `statistics-figures/`. `split.py` copies them into `docs/` automatically — never edit the copies by hand.
- Hand-written (`split.py` never touches them): `docs/index.md`, `docs/js/`,
  `docs/stylesheets/`, `mkdocs.yml`, `README.md`. Touch only when structure changes.

## What to report

- **Typo / wrong number:** quote the line, give the fix.
- **Code bug:** paste the error plus your package versions (`pip freeze | grep -Ei "numpy|pandas|scipy|statsmodels|scikit|matplotlib|seaborn"`).
- **Confusing paragraph:** say what you tripped on and how you'd say it simply.

## Code rules

- Every Python block must run top-to-bottom after `pip install -r requirements.txt`.
- Self-contained preferred. If a block continues an earlier one, start it with `# runs after the <name> block above`.
- No new dependencies without discussion.

## Preview the site locally

```bash
pip install mkdocs-material
mkdocs serve
```

Open `http://127.0.0.1:8000`.
