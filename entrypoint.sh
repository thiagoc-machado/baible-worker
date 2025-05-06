source .env
celery -A celery_app worker --loglevel=info