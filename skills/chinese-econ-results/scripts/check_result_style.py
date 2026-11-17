#!/usr/bin/env python3
"""Scan Chinese empirical-results prose for technical-output formatting.

The script reports exact p/t/z-value patterns so the writer can distinguish
single-coefficient formatting from explicitly labelled joint tests.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = {
    "p-value": re.compile(r"\bp\s*=|\bp\s*值\s*[=:：]|[（(]\s*p\s*值", re.I),
    "t-value": re.compile(r"\bt\s*=|\bt\s*值\s*[=:：]|[（(]\s*t\s*值", re.I),
    "z-value": re.compile(r"\bz\s*=|\bz\s*值\s*[=:：]|[（(]\s*z\s*值", re.I),
    "standard-error": re.compile(r"标准误|标准误差|\bse\s*=|\bstd\.??\s*err", re.I),
}


def scan(text: str) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                hits.append((line_no, label, line.strip()))
    return hits


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_result_style.py FILE", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    hits = scan(path.read_text(encoding="utf-8"))
    if not hits:
        print("PASS: no exact p/t/z-value formatting patterns found")
        return 0
    print("REVIEW: inspect the following exact-statistic patterns:")
    for line_no, label, line in hits:
        print(f"{line_no}: {label}: {line}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
