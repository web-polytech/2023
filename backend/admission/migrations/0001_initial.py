# Generated by Django 4.2.1 on 2023-05-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=255, verbose_name='ФИО заявителя')),
                ('child', models.CharField(max_length=255, verbose_name='ФИО ребёнка')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Родной город')),
                ('birth', models.DateField(verbose_name='Дата рождения ребёнка')),
                ('passport', models.FileField(upload_to='passport/', verbose_name='Сведетельство о рождении или паспорт ребёнка')),
                ('o86y', models.FileField(upload_to='o86y/', verbose_name='Справка о состоянии здоровья формы 086y')),
                ('shg', models.FileField(upload_to='shg/', verbose_name='Справка о группе здоровья')),
                ('class_field', models.CharField(max_length=255, verbose_name='Класс для поступления')),
                ('specialization', models.CharField(max_length=255, verbose_name='Специализация ребёнка (с 8 класса)')),
                ('essay', models.FileField(upload_to='essay/', verbose_name='Эссе ребёнка о своих увлечениях(от 240 слов)')),
                ('testing', models.FileField(upload_to='testing/', verbose_name='Результаты тестирования')),
                ('exam', models.FileField(upload_to='exam/', verbose_name='Результаты вступительного экзамена')),
                ('comment', models.TextField(null=True, verbose_name='Комментарий к заявке')),
                ('approval', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')),
                ('status', models.BooleanField(default=False, verbose_name='Статус рассмотрения заявки')),
            ],
            options={
                'verbose_name': 'Заявка на поступление',
                'verbose_name_plural': 'Заявки на поступление',
            },
        ),
    ]
