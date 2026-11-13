#!/bin/bash

cd /code/src/

python manage.py migrate --no-input
# python manage.py auto_admin
# python manage.py sendtestemail --admins 


RUNTIME_HOST=${RUNTIME_HOST:-0.0.0.0}
RUNTIME_PORT=${PORT:-8000}

gunicorn cicerone.wsgi:application \
    --bind $RUNTIME_HOST:$RUNTIME_PORT \
    --workers 1 \
    --threads 2 \
    --timeout 60 \
    --max-requests 1000 \
    --max-requests-jitter 100


