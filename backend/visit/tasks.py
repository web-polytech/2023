from .services import write_visit_log
from celery import shared_task

@shared_task
def write_visit_log_task():
    write_visit_log()