#!/usr/bin/env python3
"""Require minute-level author-declared timestamps on changed Markdown files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


CREATED = re.compile(r"(?:创建时间|AUTHOR_DECLARED_CREATED_AT|Created at)\s*[:：]\s*\d{4}-\d{2}-\d{2}(?:T|\s)\d{2}:\d{2}")
UPDATED = re.compile(r"(?:最后更新时间|AUTHOR_DECLARED_UPDATED_AT|Last updated at)\s*[:：]\s*\d{4}-\d{2}-\d{2}(?:T|\s)\d{2}:\d{2}")
ZONE = re.compile(r"(?:北京时间|UTC\+8|\+08:00)", re.IGNORECASE)
EXCLUDED_PARTS = {
    ".git",
    ".venv",
    ".verify-venv",
    "venv",
    "node_modules",
    "vendor",
    "third_party",
}


def changed_markdown(base: str) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", f"{base}..HEAD", "--", "*.md"],
        check=True,
        text=True,
        capture_output=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="base commit for the changed-document gate")
    args = parser.parse_args()
    errors: list[str] = []

    for path in changed_markdown(args.base):
        if any(part in EXCLUDED_PARTS for part in path.parts) or not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig")
        if not CREATED.search(text):
            errors.append(f"{path}: missing author-declared creation time to the minute")
        if not UPDATED.search(text):
            errors.append(f"{path}: missing author-declared update time to the minute")
        if not ZONE.search(text):
            errors.append(f"{path}: missing Beijing/UTC+8 timezone declaration")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] changed Markdown files contain minute-level author-declared timestamps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
