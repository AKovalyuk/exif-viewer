from celery import Celery

from app.config import get_settings


def get_celery_app() -> Celery:
    return Celery(broker=get_settings().redis_uri())


celery_app = get_celery_app()
