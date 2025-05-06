#!/bin/bash

echo "🚀 Iniciando Celery..."
celery -A celery worker --loglevel=info
