from django.urls import path
from gym.views import *

urlpatterns = [
    path ('GYMBRO', inicio, name = 'gym-inicio'),

    
    path ('pecho_plano/', vista_pecho_plano, name = 'gym-pecho_plano'),
    path ('pecho_plano/form/', form_pecho_plano, name = 'form-pecho_plano'),
    path ('pecho_plano/search/', search_pecho_plano, name = 'pecho_plano-buscar'),

    path ('pecho_inclinado/', vista_pecho_inclinado, name = 'gym-pecho_inclinado'),
    path ('pecho_inclinado/form/', form_pecho_inclinado, name = 'form-pecho_inclinado'),
    path ('pecho_inclinado/search/', search_pecho_inclinado, name = 'pecho_inclinado-buscar'),

    path ('pecho_declinado/', vista_pecho_declinado, name = 'gym-pecho_declinado'),
    path ('pecho_declinado/form/', form_pecho_declinado, name = 'form-pecho_declinado'),
    path ('pecho_declinado/search/', search_pecho_declinado, name = 'pecho_declinado-buscar')
]