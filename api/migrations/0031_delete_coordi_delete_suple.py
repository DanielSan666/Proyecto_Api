# Generated by Django 4.2.2 on 2023-07-20 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_coordi_suple'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coordi',
        ),
        migrations.DeleteModel(
            name='Suple',
        ),
    ]
