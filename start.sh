#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn --bind ":80" --workers 3 "ketzunet.wsgi:application"