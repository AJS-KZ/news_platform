#!/bin/bash
set -e

sleep 10

exec celery -A news_platform worker -l INFO --concurrency=2