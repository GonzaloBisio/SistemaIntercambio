# Generated by Django 2.2 on 2020-12-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201209_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='actividad',
            field=models.CharField(choices=[('I', 'Idiomas'), ('F', 'Financias'), ('M', 'Musica'), ('T', 'Turismo'), ('G', 'Guia')], default='T', max_length=50),
        ),
    ]