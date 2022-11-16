from django.db import models


class piernas (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)



class espalda (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)
    
class pecho (models.Model):
    maquina = models.CharField(max_length=50)
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField (blank=True)
    repeticiones = models.IntegerField (blank=True)
    series = models.IntegerField (blank=True)
