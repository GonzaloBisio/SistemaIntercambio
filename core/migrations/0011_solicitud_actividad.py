# Generated by Django 2.2 on 2020-12-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_actividad_activit'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='actividad',
            field=models.CharField(default='', max_length=50),
        ),
    ]
