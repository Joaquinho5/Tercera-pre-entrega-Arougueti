# Generated by Django 4.2.3 on 2023-08-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_tecnico_options_alter_jugador_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.IntegerField(),
        ),
    ]
