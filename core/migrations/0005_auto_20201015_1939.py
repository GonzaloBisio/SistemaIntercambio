# Generated by Django 2.2 on 2020-10-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201015_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estad',
            field=models.CharField(choices=[('NA', 'No Aprobado'), ('A', 'Aprobado')], default='R', max_length=20),
        ),
    ]