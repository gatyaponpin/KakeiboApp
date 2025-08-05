#!/bin/sh

echo "Running migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT