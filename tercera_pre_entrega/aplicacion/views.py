from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def base(request):
    return render(request, "aplicacion/base.html")

def formacion(request):
    contexto = {'Formaciones' : Formacion.objects.all()}
    return render(request, "aplicacion/formacion.html", contexto)

def formacionForm(request):
    if request.method == "POST":
        miForm = FormacionForm(request.POST)
        if miForm.is_valid():
            formacion_formacio = miForm.cleaned_data.get('formacio')
            formacion_tactica = miForm.cleaned_data.get('tactica')
            formacion = Formacion(formacio=formacion_formacio, tactica = formacion_tactica)
            formacion.save()
            contexto = {'Formaciones' : Formacion.objects.all()}
            return render(request, "aplicacion/formacion.html", contexto)
            
    else:
        miForm = FormacionForm()

    return render(request, "aplicacion/formacionForm.html", {"form": miForm})

def buscarFormacion(request):
    return render(request, "aplicacion/buscarFormacion.html")

def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Formaciones = Formacion.objects.filter(formacio__icontains=patron)
        contexto = {"Formaciones": Formaciones}
        return render(request, "aplicacion/formacion.html", contexto)
    return HttpResponse("No se ingreso nada para buscar")




def jugador(request):
    contexto = {'Jugadores': Jugador.objects.all()}
    return render(request, "aplicacion/jugador.html", contexto)

def jugadorForm2(request):
    if request.method == "POST":
        miForm = JugadorForm(request.POST)
        if miForm.is_valid():
            jugador_nombre = miForm.cleaned_data.get('nombre')
            jugador_posicion = miForm.cleaned_data.get('posicion')
            jugador = Jugador(nombre=jugador_nombre, posicion = jugador_posicion)
            jugador.save()
            contexto = {'Jugadores': Jugador.objects.all()}
            return render(request, "aplicacion\jugador.html", contexto)
    else:
        miForm = JugadorForm()

    return render(request, "aplicacion/jugadorForm2.html", {"form": miForm})

def buscarJugador(request):
    return render(request, "aplicacion/buscarJugador.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Jugadores = Jugador.objects.filter(nombre__icontains=patron)
        contexto = {"Jugadores": Jugadores}
        return render(request, "aplicacion/jugador.html", contexto)
    return HttpResponse("No se ingreso nada para buscar")

def tecnico(request):
    contexto = {'Tecnicos': Tecnico.objects.all()}
    return render(request, "aplicacion/tecnico.html", contexto)

def buscarTecnico(request):
    return render(request, "aplicacion/buscarTecnico.html")

def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Tecnicos = Tecnico.objects.filter(nombre__icontains=patron)
        contexto = {"Tecnicos": Tecnicos}
        return render(request, "aplicacion/tecnico.html", contexto)
    return HttpResponse("No se ingreso nada para buscar")



def tecnicoForm(request):
    if request.method == "POST":
        miForm = TecnicoForm(request.POST)
        if miForm.is_valid():
            tecnico_nombre = miForm.cleaned_data.get('nombre')
            tecnico_estilo = miForm.cleaned_data.get('estilo')
            tecnico = Tecnico(nombre=tecnico_nombre, estilo = tecnico_estilo)
            tecnico.save()
            contexto = {'Tecnicos': Tecnico.objects.all()}
            return render(request, "aplicacion/tecnico.html", contexto)
    else:
        miForm = TecnicoForm()

    return render(request, "aplicacion/tecnicoForm.html", {"form": miForm})


