# 📊 Basic Statistics for M.Sc Data Science

> A plain guide to statistics for data science. Each idea comes with a picture from daily life, a real use, the formula, and short Python you can run.

**📖 Read it online:** `https://<you>.github.io/basic-statistics/` *(set up Pages once — see below — then replace this line)*

![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/scipy-8CAAE6?logo=scipy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-3C3C3C?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

**~26,000 words · 8 parts + 5 appendices · 32 runnable Python examples · Beginner → Interview-ready**

## How to read

- **Online (easiest):** the link above — sidebar, search, one short page at a time.
- **Here on GitHub:** open [`docs/`](docs/) — one file per part, each small enough to render fast.
- **Single file:** [`basic statistics.md`](basic%20statistics.md) — the source of truth, good for offline or printing.

Start with [Part 1 — Descriptive](docs/part-01-descriptive.md) and [Part 2 — Probability](docs/part-02-probability.md). Everything else builds on them.

## Run the code

```bash
pip install -r requirements.txt
```

## Publish the reading site (one-time, ~10 min)

1. Create a public repo, upload everything in this folder.
2. In repo Settings → Pages, set source to **GitHub Actions**.
3. Edit `mkdocs.yml`: set `site_url` and `repo_url` to your address.
4. Push. The `Deploy docs` workflow builds and publishes automatically.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Small, plain-language fixes welcome.

## License

MIT — see [LICENSE](LICENSE).
