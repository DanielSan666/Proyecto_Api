# Generated by Django 4.2.2 on 2023-07-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_entre_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordi',
            name='fotografia',
            field=models.ImageField(upload_to='coordinadores/'),
        ),
    ]