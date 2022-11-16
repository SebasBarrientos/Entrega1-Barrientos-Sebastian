from django.urls import path
from gym.views import *

urlpatterns = [
    path ('GYMBRO', inicio, name = 'gym-inicio'),
    path ('pecho_plano/', pecho_plano, name = 'gym-pecho_plano'),
    path ('pecho_inclinado/', pecho_inclinado, name = 'gym-pecho_inclinado'),
    path ('pecho_declinado/', pecho_declinado, name = 'gym-pecho_declinado'),
]