# Generated by Django 3.1.4 on 2021-02-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0003_auto_20210201_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
