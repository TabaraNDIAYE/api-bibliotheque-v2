#!/usr/bin/env bash
set -o errexit

# Utiliser le port fourni par Render (par défaut 10000)
export PORT="${PORT:-10000}"

# Lancer Gunicorn avec des timeouts plus longs
gunicorn bibliotheque_project.wsgi:application \
    --bind "0.0.0.0:${PORT}" \
    --workers 2 \
    --timeout 120 \
    --graceful-timeout 30 \
    --log-level info