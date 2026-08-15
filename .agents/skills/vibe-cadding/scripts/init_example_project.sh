#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_NAME="${1:-example}"
PROJECT_DIR="$ROOT_DIR/projects/$PROJECT_NAME"
MODEL_PATH="$PROJECT_DIR/model.py"
TEMPLATE_PATH="$ROOT_DIR/scripts/templates/example_gears_model.py"
TEMPLATE_CACHE_DIR="$ROOT_DIR/scripts/templates/example_gears_part_cache"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install uv first: https://docs.astral.sh/uv/"
  exit 1
fi

cd "$ROOT_DIR"

echo "Installing Python dependencies with uv..."
uv sync

echo "Installing Playwright browser runtime..."
uv run playwright install chromium

mkdir -p "$PROJECT_DIR"
if [[ -e "$MODEL_PATH" ]]; then
  echo "Refusing to overwrite existing model: $MODEL_PATH"
  echo "Choose another project name, or move that file and rerun this script."
  exit 1
fi

cp "$TEMPLATE_PATH" "$MODEL_PATH"

if [[ -d "$TEMPLATE_CACHE_DIR" ]]; then
  echo "Seeding starter part cache..."
  mkdir -p "$PROJECT_DIR/.vibecad/part-cache"
  cp -R "$TEMPLATE_CACHE_DIR/." "$PROJECT_DIR/.vibecad/part-cache/"
fi

cat <<EOF

Created example vibe-cadding project:
  $MODEL_PATH

The generated model is intentionally example code and should be replaced with
the real model for the project after the viewer is up.

Start the local webserver with:
  uv run vibecad --model projects/$PROJECT_NAME/model.py --host 127.0.0.1 --port 8000

Cold start note:
  The first server launch in a fresh environment may spend a few minutes
  importing CadQuery/OCP before printing Uvicorn startup logs. Do not restart
  it during that initial silent import unless the process exits or is clearly
  not making progress.

Optional shell defaults so helper commands do not need repeated flags:
  export VIBECAD_MODEL=projects/$PROJECT_NAME/model.py
  export VIBECAD_SERVER=http://127.0.0.1:8000

Then paste this clickable link into the chat:
  Local viewer: http://127.0.0.1:8000

EOF
