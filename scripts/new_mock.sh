#!/bin/bash
# Creates a fresh practice session directory from the minimal template

set -e

SESSION_NAME=${1:-"session_$(date +%Y%m%d_%H%M%S)"}
TARGET="practice_sessions/$SESSION_NAME"

mkdir -p "$TARGET/src" "$TARGET/tests"
cp templates/python_project_template/src/app.py "$TARGET/src/app.py"
cp templates/python_project_template/tests/test_app.py "$TARGET/tests/test_app.py"

echo "Created new session at: $TARGET"
