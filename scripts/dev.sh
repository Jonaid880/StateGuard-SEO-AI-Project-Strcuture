#!/usr/bin/env bash
# Start the FastAPI backend and Next.js frontend together for local development.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Starting StateGuard backend (FastAPI) on :8000 ..."
(cd "$ROOT/services/api" && uvicorn app.main:app --reload --port 8000) &
API_PID=$!

echo "Starting StateGuard frontend (Next.js) on :3000 ..."
(cd "$ROOT/apps/web" && npm run dev) &
WEB_PID=$!

trap 'kill "$API_PID" "$WEB_PID" 2>/dev/null || true' EXIT
wait
