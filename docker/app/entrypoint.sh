#!/bin/sh
set -e

gunicorn news_platform.asgi:application -k uvicorn.workers.UvicornWorker -w $GUNICORN_WORKERS -b 0.0.0.0:8000