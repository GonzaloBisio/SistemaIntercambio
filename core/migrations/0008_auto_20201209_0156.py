# Generated by Django 2.2 on 2020-12-09 01:56

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201209_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertraveller',
            name='email',
            field=models.CharField(max_length=60, unique=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]