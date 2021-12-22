#!/bin/bash
set -e

sleep 10

exec celery -A news_platform worker --loglevel=info --concurrency=2