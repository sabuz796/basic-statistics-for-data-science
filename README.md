# 📊 Basic Statistics for M.Sc Data Science

> A plain-English guide to statistics for data science. Every idea comes with a picture
> from daily life, a real-world use, the formula, and short Python you can actually run.

![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/scipy-8CAAE6?logo=scipy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-3C3C3C?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

**~26,000 words · 8 parts + 5 appendices · 32 runnable Python examples · Beginner → Interview-ready**

**This book is free, open source, and ad-free forever. No account, no tracking, no paywall.**
If it helps you, give the repository a ⭐ so more students find it.

---

## Why this exists

Most statistics material for data science is written in one of two unhelpful ways:

- **Textbooks** — rigorous, but they assume you already speak mathematics.
- **Blog posts** — short and friendly, but they leave gaps you only discover during an interview
  or when your analysis collapses in review.

This book walks the middle. Every concept is built the same way, in this order:

1. **What it says** — one or two plain sentences first
2. **A picture from daily life** — dice, buses, sugar pills, ice-cream and sunburn
3. **Where you meet it in real work** — the data-science situation that forces you to care
4. **The formula** — with every term translated into words
5. **Short Python** — copy, run, tweak, break it

If you can write a for-loop but go quiet when someone says *"p-value"*, this book is for you.

---

## Who it is for

| You are | This helps you |
|---|---|
| An M.Sc / undergrad data-science student | Pass the stats course and the interview that follows |
| A self-taught developer moving into ML | Fill the math gaps people test you on |
| A working analyst | Correctly use, and defend, t-tests, CIs, ANOVA, regression diagnostics |
| A teacher or tutor | A free, printable coursebook with runnable examples |

**Prerequisites:** basic Python (lists, for-loops, function calls). No calculus, no linear algebra,
no prior stats. Everything else is explained on the way.

---

## Start here (recommended path)

Read in this order. **Give Parts 1 and 2 proper time — everything else is built on top of them.**

| # | Part | What you learn |
|---|---|---|
| 0 | [Orientation](docs/part-00-orientation.md) | What statistics actually is, and why "94% accuracy" means nothing on its own |
| 1 | [Descriptive Statistics](docs/part-01-descriptive.md) | Mean vs median, variance, z-scores, box plots, correlation |
| 2 | [Probability](docs/part-02-probability.md) | The three axioms, counting, conditional probability, Bayes' theorem |
| 3 | [Probability Distributions](docs/part-03-distributions.md) | Normal, binomial, Poisson, and which one to pick |
| 4 | [Sampling & Estimation](docs/part-04-sampling.md) | Sampling bias, the Central Limit Theorem, confidence intervals |
| 5 | [Hypothesis Testing](docs/part-05-testing.md) | The 5-step procedure, p-values, t-tests, chi-square, ANOVA, multiple testing |
| 6 | [Regression Analysis](docs/part-06-regression.md) | Least squares, R², diagnostics, and *why* correlation is not causation |
| 7 | [Practical Topics](docs/part-07-practical.md) | Rank tests, robust statistics, categorical data, time series, a full churn case study |

Then the [Appendices](docs/appendices.md): a one-page **formula sheet**, **cheat tables** for
every distribution and test, **practice questions with worked answers**, a **glossary**, and the
**top 20 mistakes** data scientists make.

New here? Start with [Getting Started](docs/getting-started.md) for how each idea is presented,
then work through Parts 0–7 in order and finish with the [Closing](docs/closing.md).

---

## Three ways to read it

| Way | Best for | How |
|---|---|---|
| **Online** (easiest) | Reading and searching | The published GitHub Pages site *(link below)* — sidebar, search, one short page at a time |
| **On GitHub** | Browsing the raw text | Open [`docs/`](docs/) — one small file per part, renders fast |
| **Single file** | Offline or printing | [`basic statistics.md`](basic%20statistics.md) — the whole book in one file, the source of truth |

> 📖 **Read it online:** https://sabuz796.github.io/basic-statistics-for-data-science/

---

## Run the code

Every Python block in this book is self-contained (or clearly marked as continuing an earlier
block). **All 32 examples were executed and produce the printed output shown.**

```bash
# 1. Get the book
git clone https://github.com/sabuz796/basic-statistics-for-data-science.git
cd basic-statistics-for-data-science

# 2. Install the scientific stack (Python 3.9 or newer)
pip install -r requirements.txt

# 3. Try it
python3 -c "import numpy as np; print(np.random.seed(0) or np.random.normal(100, 15, 1000)[:5])"
```

Then copy any code block from the book into a `.py` file, or run them with Jupyter:

```bash
pip install jupyter
jupyter lab
```

**Requirements:**

| Package | Version | Used for |
|---|---|---|
| numpy | ≥ 1.24 | arrays, randomness, vectors of numbers |
| pandas | ≥ 2.0 | tables, group-bys, the churn case study |
| scipy | ≥ 1.11 | distributions, t-tests, chi-square, ANOVA |
| statsmodels | ≥ 0.14 | regression output, multiple testing, ARIMA |
| scikit-learn | ≥ 1.3 | logistic regression, train/test splits |
| matplotlib | ≥ 3.7 | plots |
| seaborn | ≥ 0.12 | better-looking plots |

Nothing is behind an API or a paid service. Everything runs on your laptop in a second or two.

---

## How the book is built

```
basic statistics.md        ← SOURCE OF TRUTH: the whole book, one file
        │
        │  python3 split.py   (runs before every commit)
        ▼
docs/                      ← 11 generated pages + hand-written index/mkdocs files (12 .md files total)
        │
        │  GitHub Actions (mkdocs build --strict)
        ▼
https://sabuz796.github.io/basic-statistics-for-data-science/
```

- `basic statistics.md` — the single source of truth. **Edit this.**
- `split.py` — splits it into one page per part for the website, and syncs the figures. Run it after
  every edit (`python3 split.py`), then commit both. It uses only the Python standard library.
- `statistics-figures/` — the 32 original SVG figures. `split.py` copies them into `docs/` automatically.
- `docs/js/`, `docs/stylesheets/`, `docs/index.md`, `mkdocs.yml`, `README.md` — hand-written, never
  overwritten by `split.py`.

Nothing to build locally to *read* the book — only the website needs `mkdocs`
(see [Preview the site locally](#preview-the-site-locally)).

---

## Preview the site locally

```bash
pip install mkdocs-material
mkdocs serve
# open http://127.0.0.1:8000
```

The whole site builds in about one second, so `mkdocs serve` refreshes instantly as you edit.

---

## Publish your own copy

The publishing setup (GitHub Pages, free, HTTPS included) takes about ten minutes:

1. **Create the repository and commit**
   ```bash
   git init
   git add -A
   git commit -m "Initial commit: Basic Statistics for M.Sc Data Science"
   ```
2. **Create an empty repo on GitHub** (github.com/new — public, *do not* add a README), then:
   ```bash
   git remote add origin https://github.com/<you>/<your-repo>.git
   git branch -M main
   git push -u origin main
   ```
3. **Turn on Pages:** repo **Settings → Pages → Source: GitHub Actions** (the
   [Deploy docs](.github/workflows/deploy-docs.yml) workflow is already in this repo).
4. **Push** — the workflow builds and publishes. Your link appears under
   **Settings → Pages** (or the repo's **Actions** tab shows the deploy log).

That's it. Every later push to `main` redeploys automatically.

---

## Contribute

Small, plain-language improvements are always welcome: a typo, a clearer example, a better
explanation, one more worked answer.

- See [CONTRIBUTING.md](CONTRIBUTING.md) for the writing rules ("write like a senior explaining to
  a junior over tea") and how the files fit together.
- Found something wrong? **Open an Issue** — quote the line and say what's misleading.
- Fix something? Open a Pull Request. Keep it small and focused.

The rules that keep the book healthy:
- Every Python block must run top-to-bottom after `pip install -r requirements.txt`.
- Plain language first; the formula second.
- No new dependencies without discussion.

---

## Reuse it for your own course

This book is **MIT licensed** — you may use, adapt, translate and redistribute it, including
commercially, as long as you keep the copyright and license notice. Teaching a course on it?
Translate it into another language? Fork it, change it, make it yours. Attribution and a link
back are appreciated but not required.

---

## License

[MIT](LICENSE) © the contributors. Free for everyone, forever.

---

## Acknowledgements

Built with the tools it teaches: Python, NumPy, pandas, SciPy, statsmodels, scikit-learn,
matplotlib, and MkDocs Material.

---

*Made for students who can code but were never taught statistics. If that's you — start with
[Part 1](docs/part-01-descriptive.md) and read slowly. It gets easier fast.*
