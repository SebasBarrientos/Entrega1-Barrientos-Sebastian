# Generated by Django 4.1.3 on 2022-11-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pecho_declinado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.IntegerField()),
                ('nombre_ejercicio', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pecho_inclinado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.IntegerField()),
                ('nombre_ejercicio', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pecho_plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.IntegerField()),
                ('nombre_ejercicio', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
            ],
        ),
    ]
