# Generated by Django 4.2.1 on 2023-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_alter_visit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='get_params',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='os',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='visit',
            name='post_params',
            field=models.TextField(blank=True),
        ),
    ]