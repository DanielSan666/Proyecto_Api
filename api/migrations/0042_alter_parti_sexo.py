# Generated by Django 4.2.2 on 2023-08-04 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_alter_parti_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parti',
            name='sexo',
            field=models.CharField(blank=True, choices=[('', '--Seleccione el sexo--'), ('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='', max_length=150, null=True),
        ),
    ]
