# /usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python wordle-collab/manage.py'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --noinput

echo 'Migrating database...'
$RUN_MANAGE_PY migrate --noinput

exec poetry run daphne wordle-collab.core.asgi:application --port 8000 --bind 0.0.0.0