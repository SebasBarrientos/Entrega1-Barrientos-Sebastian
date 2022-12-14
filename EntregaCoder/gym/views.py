from django.http import HttpResponse
from gym.models import *


from django.shortcuts import render
from gym.forms import *

# Create your views here.
def inicio (request):
    return render(request, 'gym/base.html')





def form_piernas (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = piernas (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_piernas.html', contexto)

def vista_piernas (request):
    return render (request, 'gym/piernas.html')

def buscador_piernas (request):
    return render (request, 'gym/buscador_piernas.html')


def resultado_piernas (request):
    nombre= request.GET ["nombre_ejercicio"]
    ejercicios = piernas.objects.filter (nombre_ejercicio__icontains=nombre)

    return render (request, 'gym/resultado_piernas.html', {'ejercicios': ejercicios})




def form_espalda (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = espalda (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_espalda.html', contexto)

def vista_espalda (request):
    return render (request, 'gym/espalda.html')




def buscador_espalda (request):
    return render (request, 'gym/buscador_espalda.html')


def resultado_espalda (request):
    nombre= request.GET ["nombre_ejercicio"]
    ejercicios = espalda.objects.filter (nombre_ejercicio__icontains=nombre)

    return render (request, 'gym/resultado_espalda.html', {'ejercicios': ejercicios})








def form_pecho (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = pecho (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_pecho.html', contexto)


def vista_pecho (request):

    return render (request, 'gym/pecho.html')

def buscador_pecho (request):
    return render (request, 'gym/buscador_pecho.html')


def resultado_pecho (request):
    nombre= request.GET ["nombre_ejercicio"]
    ejercicios = pecho.objects.filter (nombre_ejercicio__icontains=nombre)

    return render (request, 'gym/resultado_pecho.html', {'ejercicios': ejercicios})