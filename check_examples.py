"""Run every ```python block in `basic-statistics.md` top-to-bottom.

CI runs this on every push and weekly (see .github/workflows/check-examples.yml),
so the book's claim that all 32 examples run keeps being true as dependencies move.

    python3 check_examples.py

Blocks share one namespace and run in document order, so a block marked
`# runs after the <name> block above` works as documented in CONTRIBUTING.md.
Mark a genuinely unrunnable block with `# skip-ci` as a comment in the block.
"""

import os
import re
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "basic-statistics.md"


def main() -> int:
    # headless plots before any block imports matplotlib
    os.environ.setdefault("MPLBACKEND", "Agg")
    blocks = re.findall(r"^```python\n(.*?)^```", SRC.read_text(), re.M | re.S)
    if not blocks:
        print(f"no python blocks found in {SRC.name}", file=sys.stderr)
        return 1

    namespace = {}
    failed = []
    for i, code in enumerate(blocks, 1):
        if "# skip-ci" in code:
            print(f"block {i}: skipped (# skip-ci)")
            continue
        first = next((ln.strip() for ln in code.splitlines() if ln.strip()), "?")
        try:
            exec(compile(code, f"{SRC.name} block {i}", "exec"), namespace)
        except Exception:
            failed.append(i)
            print(f"block {i} FAILED: {first}", file=sys.stderr)
            traceback.print_exc(limit=3, file=sys.stderr)

    ran = len(blocks) - len(failed)
    print(f"{ran}/{len(blocks)} blocks ran")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
