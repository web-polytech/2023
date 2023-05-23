from django.db import models
from news.models import News


class Quote(models.Model):
    news_id = models.ForeignKey(
        verbose_name="Новость",
        to=News,
        on_delete=models.CASCADE,
        related_name='quote')
    name = models.CharField(verbose_name="Автор цитаты", max_length=200)
    text = models.TextField(verbose_name="Текст цитаты")
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='news_covers',
        null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
