# Generated by Django 4.2.2 on 2023-06-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_delete_uni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uni',
            fields=[
                ('uniId', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=150)),
                ('universidad', models.CharField(max_length=150)),
                ('clave', models.BigIntegerField()),
                ('camiones', models.IntegerField()),
                ('vans', models.IntegerField()),
                ('carros', models.IntegerField()),
                ('hotel', models.CharField(max_length=150)),
                ('requerimientos', models.CharField(max_length=150)),
                ('guias', models.IntegerField()),
                ('fotografia', models.ImageField(upload_to='universidad/')),
                ('carta_protes', models.FileField(upload_to='archivos/')),
            ],
        ),
    ]
