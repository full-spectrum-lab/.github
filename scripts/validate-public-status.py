#!/usr/bin/env python3
"""Validate Full Spectrum Lab's machine-readable public status record."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS_FILE = ROOT / "status" / "public-status.json"
PROFILE_FILES = [ROOT / "profile" / "README.md", ROOT / "profile" / "README.zh-CN.md"]
SEMVER = re.compile(r"^v\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def check_url(url: str, errors: list[str]) -> None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "full-spectrum-status-check"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            require(response.status < 400, f"URL returned {response.status}: {url}", errors)
    except (urllib.error.URLError, TimeoutError) as exc:
        errors.append(f"URL unavailable: {url}: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="also verify public release URLs")
    args = parser.parse_args()
    errors: list[str] = []
    data = json.loads(STATUS_FILE.read_text(encoding="utf-8"))

    require(data.get("schema_version") == "1.0", "schema_version must be 1.0", errors)
    require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", data.get("updated_at", ""))), "updated_at must be YYYY-MM-DD", errors)
    projects = data.get("projects", {})
    for name in ("engine", "observer", "protocol", "industrial_case"):
        require(name in projects, f"missing project status: {name}", errors)

    engine = projects.get("engine", {})
    observer = projects.get("observer", {})
    for key in ("stable_release", "preview_release"):
        require(bool(SEMVER.fullmatch(engine.get(key, ""))), f"invalid engine {key}", errors)
    for key in ("latest_release", "development_version"):
        require(bool(SEMVER.fullmatch(observer.get(key, ""))), f"invalid observer {key}", errors)
    require("NOT_RELEASED" in observer.get("development_status", ""), "Observer development line must say NOT_RELEASED", errors)

    industrial = projects.get("industrial_case", {})
    require(industrial.get("production_validated") is False, "industrial case must not claim production validation", errors)
    require(industrial.get("named_customer") is False, "industrial case must not claim a named customer", errors)

    profiles = "\n".join(path.read_text(encoding="utf-8") for path in PROFILE_FILES)
    for value in (engine.get("stable_release"), engine.get("preview_release"), observer.get("latest_release"), observer.get("development_version")):
        require(bool(value and value in profiles), f"profile does not mention {value}", errors)

    if args.online:
        for url in (engine["stable_release_url"], engine["preview_release_url"], observer["latest_release_url"]):
            check_url(url, errors)

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] public status is structurally and semantically consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
