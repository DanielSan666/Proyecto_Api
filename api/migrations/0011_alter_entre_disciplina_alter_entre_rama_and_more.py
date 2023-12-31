# Generated by Django 4.2.2 on 2023-06-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_entre_disciplina_alter_entre_rama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entre',
            name='disciplina',
            field=models.CharField(blank=True, choices=[('', '-- Seleccione una disciplina --'), ('Ajedrez', 'Ajedrez'), ('Atletismo', 'Atletismo '), ('Baloncesto', 'Baloncesto'), ('Canto', 'Canto'), ('Declamacion', 'Declamacion'), ('Oratoria', 'Oratoria'), ('Voleibol', 'Voleibol'), ('Taekwondo', 'Taekwondo'), ('Mural en gis', 'Mural en gis'), ('Softbol', 'Softbol'), ('Rondalla', 'Rondalla'), ('Fútbol 7', 'Fútbol 7'), ('Futbol asociacion', 'Futbol asociacion')], default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='entre',
            name='rama',
            field=models.CharField(blank=True, choices=[('', '-- Seleccione una Rama --'), ('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='parti',
            name='disciplina',
            field=models.CharField(blank=True, choices=[('', '-- Seleccione una disciplina --'), ('Ajedrez', 'Ajedrez'), ('Atletismo', 'Atletismo '), ('Baloncesto', 'Baloncesto'), ('Canto', 'Canto'), ('Declamacion', 'Declamacion'), ('Oratoria', 'Oratoria'), ('Voleibol', 'Voleibol'), ('Taekwondo', 'Taekwondo'), ('Mural en gis', 'Mural en gis'), ('Softbol', 'Softbol'), ('Rondalla', 'Rondalla'), ('Fútbol 7', 'Fútbol 7'), ('Futbol asociacion', 'Futbol asociacion')], default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='parti',
            name='rama',
            field=models.CharField(blank=True, choices=[('', '-- Seleccione una Rama --'), ('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='', max_length=150, null=True),
        ),
    ]
