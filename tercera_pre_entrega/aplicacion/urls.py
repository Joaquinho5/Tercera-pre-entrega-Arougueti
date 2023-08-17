from django.urls import path, include
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('jugador/', jugador, name="jugador"),
    path('buscarJugador/', buscarJugador, name="buscarJugador"),
    path('jugador_form2/', jugadorForm2, name="jugador_form2"),
    path('formacion/', formacion, name="formacion"),
    path('formacion_form/', formacionForm, name="formacion_form"),
    path('buscarFormacion/', buscarFormacion, name="buscarFormacion"),
    path('tecnico/', tecnico, name="tecnico"),
    path('tecnico_form/', tecnicoForm, name="tecnico_form"),
    path('buscarTecnico/', buscarTecnico, name="buscarTecnico"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar4/', buscar4, name="buscar4"),
    
]