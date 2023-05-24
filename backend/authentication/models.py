from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import UserManager
from datetime import date
from admission.models import Admission


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    name = models.CharField(verbose_name="Имя", max_length=255)
    users_image = models.ImageField(
        verbose_name="Фото пользователя", upload_to="user_image", default=False
    )
    start_education = models.DateField(
        verbose_name="Начало обучения", default=date.today
    )
    end_education = models.DateField(verbose_name="Дата выпуска", null=True)
    mentor = models.ForeignKey(
        verbose_name="Классный руководитель",
        to="self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    score = models.DecimalField(
        verbose_name="Средний балл", decimal_places=2, max_digits=5, null=True
    )
    specialization = models.CharField(verbose_name="Специализация", max_length=255)
    status = models.ForeignKey(to=Admission, on_delete=models.CASCADE, null=True)

    is_active = models.BooleanField(verbose_name="Активирован", default=False)
    is_staff = models.BooleanField(verbose_name="Персонал", default=False)
    is_superuser = models.BooleanField(verbose_name="Администратор", default=False)
    is_client = models.BooleanField(verbose_name="Клиент", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "specialization"]

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
