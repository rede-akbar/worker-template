from celery import Celery
import os

os.environ.setdefault('WORKER_MODULE', 'config.dev')

CONFIG = os.environ.get('WORKER_MODULE')

app = Celery('WORKER')
app.config_from_object(CONFIG)



app.autodiscover_tasks()
