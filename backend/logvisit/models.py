from django.db import models
from django.conf import settings

class LogVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=500)
    get_params = models.TextField(blank=True)
    post_params = models.TextField(blank=True)
    browser = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Лог посещения"
        verbose_name_plural = "Логи посещений"
