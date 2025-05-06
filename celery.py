from celery import Celery
import os
from dotenv import load_dotenv

# força o caminho do .env na raiz do container
load_dotenv(dotenv_path='/app/.env')

app = Celery('app', broker=os.getenv('CELERY_BROKER_URL'))
app.autodiscover_tasks(['app'])
