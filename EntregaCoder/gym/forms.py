from django import forms

class Formulario (forms.Form):
    maquina = forms.CharField ()
    nombre_ejercicio = forms.CharField()
    peso = forms.IntegerField ()
    repeticiones = forms.IntegerField ()
    series = forms.IntegerField ()
