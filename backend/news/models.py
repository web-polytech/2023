from django.db import models
from datetime import date

class News(models.Model):
    cover = models.ImageField(verbose_name='Обложка новости',upload_to='news_covers')
    title = models.CharField(verbose_name='Название',max_length=255)
    tagline = models.CharField(verbose_name='Категория',max_length=255)
    lid = models.TextField(verbose_name='Лид',)
    text = models.TextField(verbose_name='Текст новости',)
    date = models.DateField(verbose_name='Дата публикации',default=date.today)
    duration = models.IntegerField(verbose_name="Длительность чтения",default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
