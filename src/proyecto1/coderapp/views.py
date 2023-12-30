from django.shortcuts import render
from django.http import HttpResponse

from coderapp.models import Profesor

def leer_profesor(request):

    profe = Profesor(nombre = "Carlos", apellido = "Juarez", email = "amsda@asd.com")

    profe.save()

    return HttpResponse("vista profesor")

def leer_alumnos(request):

    contexto = {
        "nombre": "Ramiro",
        "edad": 50,
        "cursos": ["Python", "Java", "JS"],
    }

    http = render(request, "template1.html", contexto)
    return HttpResponse(http)

def index(request):
    return render(request, "index.html")

def profesor(request):
    return HttpResponse("Vista profesor")

def estudiante(request):
    return HttpResponse("Vista estudiante")

def curso(request):
    return HttpResponse("Vista curso")

def entregable(request):
    return HttpResponse("Vista entregable")
