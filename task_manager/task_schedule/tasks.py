from celery import shared_task
@shared_task
def add_two(x, y):
    return x + y