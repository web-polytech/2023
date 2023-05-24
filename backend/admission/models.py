from django.db import models


class Admission(models.Model):
    parent = models.CharField(verbose_name="ФИО заявителя", max_length=255)
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

    def __str__(self):
        return "Admission form for {}".format(self.child)

    class Meta:
        verbose_name = "Заявка на поступление"
        verbose_name_plural = "Заявки на поступление"
