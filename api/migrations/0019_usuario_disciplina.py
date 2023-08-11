# Generated by Django 4.2.2 on 2023-07-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_parti_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='disciplina',
            field=models.CharField(blank=True, choices=[('', '-- Seleccione una disciplina --'), ('Ajedrez', 'Ajedrez'), ('Atletismo', 'Atletismo '), ('Baloncesto', 'Baloncesto'), ('Canto', 'Canto'), ('Declamacion', 'Declamacion'), ('Oratoria', 'Oratoria'), ('Voleibol', 'Voleibol'), ('Taekwondo', 'Taekwondo'), ('Mural en gis', 'Mural en gis'), ('Softbol', 'Softbol'), ('Rondalla', 'Rondalla'), ('Fútbol 7', 'Fútbol 7'), ('Futbol asociacion', 'Futbol asociacion')], default='', max_length=150, null=True),
        ),
    ]