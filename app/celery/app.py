from celery import Celery

from app.config import get_settings


def get_celery_app() -> Celery:
    return Celery(broker='')


celery_app = get_celery_app()
