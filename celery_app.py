from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

app = Celery(
    'baible_worker',
    broker=os.getenv('CELERY_BROKER_URL')
)

app.autodiscover_tasks(['tasks'])