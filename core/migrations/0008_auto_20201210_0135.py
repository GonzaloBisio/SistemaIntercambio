# Generated by Django 2.2 on 2020-12-10 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201210_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='actividad',
            field=models.CharField(default='', max_length=50),
        ),
    ]