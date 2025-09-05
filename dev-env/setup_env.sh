#!/bin/bash
# dev-env/setup.sh: Set up Python virtual environment in repo root and install requirements

set -e

# Get the directory of this script and the repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$REPO_ROOT/.venv"
REQ_FILE="$REPO_ROOT/requirements.txt"

# Check if .venv exists in repo root
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists in $VENV_DIR."
fi

# Activate venv and install requirements
source "$VENV_DIR/bin/activate"
if [ -f "$REQ_FILE" ]; then
    echo "Installing requirements from $REQ_FILE..."
    pip install --upgrade pip
    pip install -r "$REQ_FILE"
else
    echo "No requirements.txt found. Skipping package installation."
fi

echo "Development environment setup complete."
