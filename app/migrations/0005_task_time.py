# Generated by Django 3.1 on 2021-05-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default='12-3-2020'),
        ),
    ]
