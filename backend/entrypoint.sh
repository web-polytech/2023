#!/usr/bin/env bash

# python manage.py flush --no-input
python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input

exec "$@"
