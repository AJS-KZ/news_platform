import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_platform.settings')
celery_app = Celery('news_platform')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
