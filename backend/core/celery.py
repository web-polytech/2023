import os
import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admission.settings")

app = celery.Celery("admission")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Добавляем параметры конфигурации для Flower:
app.conf.update(
    broker_url=os.environ.get("CELERY_BROKER_URL", "pyamqp://guest@localhost//"),
    result_backend=os.environ.get("CELERY_RESULT_BACKEND", "rpc://"),
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    worker_prefetch_multiplier=1,
)
