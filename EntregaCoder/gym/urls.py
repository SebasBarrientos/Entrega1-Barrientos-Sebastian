from django.urls import path
from gym.views import *

urlpatterns = [
    path ('GYMBRO', inicio, name = 'gym-inicio'),
    
    path ('piernas/', vista_piernas, name = 'gym-piernas'),
    path ('piernas/form/', form_piernas, name = 'form-piernas'),
    path ('piernas/buscador/', buscador_piernas, name = 'piernas-buscar'),
    path ('piernas/buscador/resultados/', resultado_piernas, name = 'resultado-piernas'),

    path ('espalda/', vista_espalda, name = 'gym-espalda'),
    path ('espalda/form/', form_espalda, name = 'form-espalda'),
    path ('espalda/buscador/', buscador_espalda, name = 'espalda-buscar'),
    path ('espalda/buscador/resultado', resultado_espalda, name = 'espalda-resultado'),


    path ('pecho/', vista_pecho, name = 'gym-pecho'),
    path ('pecho/form/', form_pecho, name = 'form-pecho'),
    path ('pecho/buscador/', buscador_pecho, name = 'pecho-buscar'),
    path ('pecho/buscador/resultado', resultado_pecho, name = 'pecho-resultado'),
]