# Generated by Django 2.2 on 2020-12-03 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201201_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerhost',
            name='registertraveller_ptr',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Hospedador',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
        migrations.DeleteModel(
            name='RegisterHost',
        ),
    ]