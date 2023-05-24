from django.db import models
from news.models import News


class Gallery(models.Model):
    photo_gallery = models.ImageField(upload_to="news_covers")
    news_id = models.ForeignKey(
        verbose_name="новость",
        to=News,
        on_delete=models.CASCADE,
        related_name="gallery",
    )
    description = models.CharField(
        verbose_name="Описание фотографии", max_length=255, default=None
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
