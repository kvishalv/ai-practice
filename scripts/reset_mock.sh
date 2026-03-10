#!/bin/bash
# Resets a practice session directory back to the blank template

set -e

SESSION_NAME=${1:-""}

if [ -z "$SESSION_NAME" ]; then
  echo "Usage: $0 <session_name>"
  exit 1
fi

TARGET="practice_sessions/$SESSION_NAME"

if [ ! -d "$TARGET" ]; then
  echo "Session not found: $TARGET"
  exit 1
fi

cp templates/python_project_template/src/app.py "$TARGET/src/app.py"
cp templates/python_project_template/tests/test_app.py "$TARGET/tests/test_app.py"

echo "Reset session: $TARGET"
