# Generated by Django 5.1.1 on 2024-09-26 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quest',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]
