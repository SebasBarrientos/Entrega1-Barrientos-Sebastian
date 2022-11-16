# Generated by Django 4.1.3 on 2022-11-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_pecho_declinado_repeticiones_pecho_declinado_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pecho_declinado',
            name='maquina',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pecho_declinado',
            name='peso',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_declinado',
            name='repeticiones',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_declinado',
            name='series',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_inclinado',
            name='maquina',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pecho_inclinado',
            name='peso',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_inclinado',
            name='repeticiones',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_inclinado',
            name='series',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pecho_plano',
            name='maquina',
            field=models.CharField(max_length=50),
        ),
    ]