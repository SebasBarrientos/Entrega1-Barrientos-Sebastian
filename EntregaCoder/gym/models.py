from django.db import models


class pecho_plano (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)



class pecho_inclinado (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)
    
class pecho_declinado (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)
