# Generated by Django 4.1.1 on 2022-10-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.BooleanField(default=False),
        ),
    ]
