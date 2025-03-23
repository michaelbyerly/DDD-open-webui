#!/bin/bash

# Optional: activate conda env
# eval "$(conda shell.bash hook)"
# conda activate open-webui

# Function to install a package if it's missing
install_if_missing() {
    python3 -c "import $1" 2>/dev/null || {
        echo "Missing: $1. Installing..."
        pip install "$2"
    }
}

# List of packages: format is import_name=pip_name
install_if_missing uvicorn uvicorn
install_if_missing fastapi fastapi
install_if_missing requests requests
install_if_missing pydantic pydantic
install_if_missing openai openai
# Add more as needed

# Run the server
PORT="${PORT:-8080}"
uvicorn open_webui.main:app \
  --port "$PORT" \
  --host 0.0.0.0 \
  --forwarded-allow-ips '*' \
  --reload
