# Generated by Django 2.2.6 on 2019-10-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0002_auto_20191021_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nome',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
