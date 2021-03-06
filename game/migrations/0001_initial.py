# Generated by Django 3.1.4 on 2020-12-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='описание')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='email')),
                ('phone', models.CharField(max_length=120, verbose_name='Telephone')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
    ]
