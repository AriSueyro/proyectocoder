from django.shortcuts import render
from django.http import HttpResponse

from coderapp.models import Profesor, Curso
from coderapp.forms import CursoFormulario

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
    
    contexto = {
        "nombre": "Ramiro",
        "edad": 50,
        "cursos": ["Python", "Java", "JS"],
    }
    
    return render(request, "profesor.html", contexto)

def estudiante(request):
    return render(request, "estudiante.html")

def curso(request):
    return render(request, "curso.html")

def entregable(request):
    return render(request, "entregable.html")

def formulario(request):
    
    if request.method == "POST": 
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
        

        curso = Curso(nombre = datos.get("curso"), camada = datos.get("camada"))
        curso.save()

        return render(request, "index.html")

    return render(request, "formulario.html")