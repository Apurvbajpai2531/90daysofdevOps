from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0"
)

@celery.task
def heavy_task():
    return "Background task executed!"

