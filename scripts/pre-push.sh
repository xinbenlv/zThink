#!/bin/sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

if ! command -v bundle >/dev/null 2>&1; then
  echo "pre-push: bundler is required" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "pre-push: python3 is required" >&2
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "pre-push: npx is required" >&2
  exit 1
fi

exec sh scripts/lighthouse-audit.sh --strategy=mobile
