# Generated by Django 4.1.5 on 2023-01-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurerhistory',
            name='consumption',
            field=models.FloatField(default=0),
        ),
    ]
