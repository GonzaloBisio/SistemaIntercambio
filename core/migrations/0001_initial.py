# Generated by Django 2.2 on 2020-12-08 19:09

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
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(default='', max_length=20)),
                ('estado', models.CharField(default='', max_length=20)),
                ('domicilio', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('NA', 'No Aprobado'), ('A', 'Aprobado')], default='NA', max_length=20)),
                ('telefono', models.IntegerField()),
                ('pais', models.CharField(default='', max_length=50)),
                ('ciudad', models.CharField(default='', max_length=50)),
                ('edad', models.IntegerField()),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('viajante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterTraveller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
