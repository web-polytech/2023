from django.db import models
from authentication.models import User
from datetime import date


class Achievement(models.Model):
    user_id = models.ForeignKey(
        verbose_name="Участник",
        to=User,
        on_delete=models.CASCADE,
        related_name='achievements')
    level = models.IntegerField(verbose_name="Место", default=0)
    title = models.CharField(
        verbose_name="Название мероприятия",
        max_length=255)
    years = models.DateField(
        verbose_name="Дата проведения",
        default=date.today)

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title
