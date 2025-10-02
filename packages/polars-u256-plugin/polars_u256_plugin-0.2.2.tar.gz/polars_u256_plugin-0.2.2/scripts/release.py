#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "tomli>=2; python_version<'3.11'",
# ]
# ///

"""Simple release helper.

Usage:
  uv run scripts/release.py --check           # verify versions & state
  uv run scripts/release.py --tag vX.Y.Z      # create git tag and push

It verifies that Cargo.toml and pyproject.toml versions match and that the
working tree is clean. It does not build artifacts; CI handles that.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

try:
    import tomllib as tomli  # py311+
except Exception:  # pragma: no cover
    import tomli  # type: ignore


ROOT = Path(__file__).resolve().parents[1]


def read_toml(path: Path) -> dict:
    with path.open('rb') as f:
        return tomli.load(f)


def get_versions() -> tuple[str, str]:
    cargo = read_toml(ROOT / 'Cargo.toml')
    py = read_toml(ROOT / 'pyproject.toml')
    return cargo['package']['version'], py['project']['version']


def git(*args: str) -> str:
    out = subprocess.check_output(['git', *args], cwd=ROOT)
    return out.decode().strip()


def require_clean_worktree() -> None:
    status = git('status', '--porcelain')
    if status:
        print('ERROR: Working tree not clean:\n' + status)
        sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--tag', metavar='TAG', help='e.g., v0.2.2')
    ns = ap.parse_args()

    cargo_v, py_v = get_versions()
    if cargo_v != py_v:
        print(f'ERROR: Version mismatch Cargo.toml={cargo_v} vs pyproject.toml={py_v}')
        return 2
    print(f'Version OK: {cargo_v}')

    if ns.check:
        require_clean_worktree()
        print('Worktree clean. Ready to tag.')
        return 0

    if ns.tag:
        require_clean_worktree()
        if not ns.tag.endswith(cargo_v):
            print(f'WARNING: Tag {ns.tag} does not match version {cargo_v}.')
        print(f'Creating tag {ns.tag} ...')
        git('tag', ns.tag)
        print('Pushing tag ...')
        git('push', 'origin', ns.tag)
        print('Done. CI should build and upload to PyPI.')
        return 0

    ap.print_help()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

