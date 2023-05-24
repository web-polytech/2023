from django.db import models


class Event(models.Model):
    cover = models.ImageField(verbose_name="Обложка новости", upload_to="event_covers")
    title = models.CharField(verbose_name="Название", max_length=255)
    tagline = models.CharField(verbose_name="Категория", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
