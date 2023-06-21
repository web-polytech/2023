from django.db import models
from django.conf import settings

class Visit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=500)
    get_params = models.TextField(blank=True)
    post_params = models.TextField(blank=True)
    browser = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"
