#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if command -v poetry >/dev/null 2>&1; then
  echo "Installing pre-commit via Poetry..."
  poetry add --dev pre-commit -n
  poetry run pre-commit install
  echo "Pre-commit installed in Poetry environment."
else
  echo "Installing pre-commit via pip..."
  python -m pip install --upgrade pip
  python -m pip install pre-commit
  pre-commit install
  echo "Pre-commit installed and hooks registered."
fi
