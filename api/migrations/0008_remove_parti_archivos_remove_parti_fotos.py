# Generated by Django 4.2.2 on 2023-06-15 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_parti_fotos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parti',
            name='archivos',
        ),
        migrations.RemoveField(
            model_name='parti',
            name='fotos',
        ),
    ]
