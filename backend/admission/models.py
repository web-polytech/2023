from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache


class Admission(models.Model):
    parent = models.CharField(verbose_name="ФИО заявителя", max_length=255)
    parent_email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    child = models.CharField(verbose_name="ФИО ребёнка", max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=255)
    city = models.CharField(verbose_name="Родной город", max_length=255)
    birth = models.DateField(verbose_name="Дата рождения ребёнка")
    passport = models.FileField(
        verbose_name="Сведетельство о рождении или паспорт ребёнка",
        upload_to="passport/",
    )
    o86y = models.FileField(
        verbose_name="Справка о состоянии здоровья формы 086y", upload_to="o86y/"
    )
    shg = models.FileField(verbose_name="Справка о группе здоровья", upload_to="shg/")
    class_field = models.CharField(verbose_name="Класс для поступления", max_length=255)
    specialization = models.CharField(
        verbose_name="Специализация ребёнка (с 8 класса)", max_length=255
    )
    essay = models.FileField(
        verbose_name="Эссе ребёнка о своих увлечениях(от 240 слов)", upload_to="essay/"
    )
    testing = models.FileField(
        verbose_name="Результаты тестирования", upload_to="testing/"
    )
    exam = models.FileField(
        verbose_name="Результаты вступительного экзамена", upload_to="exam/"
    )
    comment = models.TextField(verbose_name="Комментарий к заявке", null=True)
    approval = models.BooleanField(
        verbose_name="Согласие на обработку персональных данных", default=False
    )
    status = models.BooleanField(
        verbose_name="Статус рассмотрения заявки", default=False
    )

    def send_email(self):
        subject = "Заявка на поступление в школу"
        message = f"Заявка {self.child} была изменена"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.parent_email]
        send_mail(subject, message, from_email, recipient_list)

    def __str__(self):
        return "Admission form for {}".format(self.child)

    class Meta:
        verbose_name = "Заявка на поступление"
        verbose_name_plural = "Заявки на поступление"


@receiver(post_save, sender=Admission)
def admission_saved(sender, instance, **kwargs):
    if not kwargs.get("raw", False) and instance.status:
        instance.send_email()
        print("Email sent!")
