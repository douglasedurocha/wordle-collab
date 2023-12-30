# /usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python wordle-collab/manage.py'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Migrating database...'
$RUN_MANAGE_PY migrate --noinput

echo 'Adding wordle-collab to PYTHONPATH...'
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/wordle-collab"

echo 'Setting DJANGO_SETTINGS_MODULE...'
export DJANGO_SETTINGS_MODULE="core.settings"

echo 'Starting server...'
exec poetry run daphne wordle-collab.core.asgi:application --port 8000 --bind 0.0.0.0