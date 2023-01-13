# Generated by Django 4.1.5 on 2023-01-13 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurer',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('consumption', models.BigIntegerField(default=0)),
                ('last_modification', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.BigIntegerField(default=0)),
                ('modification_time', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirest.measurer', verbose_name='Measurer historical model')),
            ],
        ),
    ]
