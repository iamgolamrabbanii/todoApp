# Generated by Django 5.1.4 on 2025-02-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='endtime',
            field=models.TimeField(default='00.00'),
        ),
    ]
