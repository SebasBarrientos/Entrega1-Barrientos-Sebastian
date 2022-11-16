from django.db import models

# Create your models here.
class pecho_plano (models.Model):
    maquina = models.IntegerField ()
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField ()




class pecho_inclinado (models.Model):
    maquina = models.IntegerField ()
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField ()
    

    
class pecho_declinado (models.Model):
    maquina = models.IntegerField ()
    nombre_ejercicio = models.CharField(max_length=50)
    peso = models.IntegerField ()
    