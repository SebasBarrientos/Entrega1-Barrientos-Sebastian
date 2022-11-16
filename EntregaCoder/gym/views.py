from django.http import HttpResponse
from gym.models import *


from django.shortcuts import render
from gym.forms import *

# Create your views here.
def inicio (request):
    return render(request, 'gym/base.html')





def form_pecho_plano (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = pecho_plano (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_pecho_plano.html', contexto)

def vista_pecho_plano (request):
    return render (request, 'gym/pecho_plano.html')

def buscador_pecho_plano (request):
    return render (request, 'gym/buscador_pecho_plano.html')


def resultado_pecho_plano (request):
    nombre_maquina = request.GET ["maquina_pecho_plano"]
    maquina = pecho_plano.objects.filter (maquina__icontains=nombre_maquina)

    return render (request, 'gym/resultado_search_pecho_plano.html', {'maquina': maquina})




def form_pecho_inclinado (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = pecho_inclinado (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_pecho_inclinado.html', contexto)

def vista_pecho_inclinado (request):

    return render (request, 'gym/pecho_inclinado.html')

def buscador_pecho_inclinado (request):
    return render (request, 'gym/buscador_pecho_inclinado.html')

def resultado_pecho_inclinado (request):
    pass






def form_pecho_declinado (request):
    if request.method == 'POST':
        formulario = Formulario (request.POST)
        
        if formulario.is_valid (): 
            data = formulario.cleaned_data
            form = pecho_declinado (maquina = data ['maquina'],nombre_ejercicio = data ['nombre_ejercicio'],peso = data ['peso'],repeticiones = data ['repeticiones'],series = data ['series'])
            form.save()
        
    formulario = Formulario()
    
    contexto = {'formulario': formulario}
    return render(request, 'gym/form_pecho_declinado.html', contexto)


def vista_pecho_declinado (request):

    return render (request, 'gym/pecho_declinado.html')

def buscador_pecho_declinado (request):
    return render (request, 'gym/buscador_pecho_declinado.html')

def resultado_pecho_declinado(request):
    pass