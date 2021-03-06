# Generated by Django 2.2.6 on 2019-10-21 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.TextField(blank=True, max_length=500)),
                ('cidade', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('dt_nascimento', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(blank=True, max_length=500)),
                ('conduta', models.TextField(blank=True, max_length=500)),
                ('cid', models.CharField(blank=True, max_length=30)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorio.Paciente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
