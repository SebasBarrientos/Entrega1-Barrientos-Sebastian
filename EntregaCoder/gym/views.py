from django.http import HttpResponse

#from gym.models import Curso, Profesor

from django.shortcuts import render
from gym.forms import *

# Create your views here.
def inicio (request):
    return render(request, 'gym/base.html')

def pecho_plano (request):
    return render (request, 'gym/pecho_plano.html')


def pecho_inclinado (request):

    return render (request, 'gym/pecho_inclinado.html')


def pecho_declinado (request):

    return render (request, 'gym/pecho_declinado.html')