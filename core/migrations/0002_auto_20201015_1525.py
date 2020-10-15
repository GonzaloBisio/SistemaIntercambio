# Generated by Django 2.2 on 2020-10-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('NR', 'No registrado'), ('R', 'Registrado'), ('ET', 'En trámite'), ('EV', 'Esperando vuelo')], default='No registrado', max_length=2)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='registertraveller',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registertraveller',
            name='status',
            field=models.CharField(choices=[('NR', 'No registrado'), ('R', 'Registrado'), ('ET', 'En trámite'), ('EV', 'Esperando vuelo')], default='No registrado', max_length=2),
        ),
    ]
