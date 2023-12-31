# Generated by Django 4.2.2 on 2023-07-06 02:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_entre_telefono_ofic_alter_entre_celular_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entre',
            old_name='Telefono_ofic',
            new_name='telefono_ofic',
        ),
        migrations.AlterField(
            model_name='entre',
            name='celular',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El número de teléfono móvil debe tener entre 9 y 15 dígitos.', regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]
