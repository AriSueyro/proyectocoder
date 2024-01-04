from django.shortcuts import render
from django.http import HttpResponse

from coderapp.models import Profesor, Curso, Entregable, Estudiante
from coderapp.forms import CursoFormulario, EntregableFormulario, EstudianteFormulario

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

    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante(nombre = datos.get("nombre"), apellido = datos.get("apellido"), email = datos.get("email"))
            estudiante.save()

            return render(request, "index.html")
        
    else:
        formulario = EstudianteFormulario()     


    return render(request, "estudiante.html", {"formulario": formulario})

def curso(request):
    return render(request, "curso.html")

def entregable(request):

    if request.method == "POST":
        formulario = EntregableFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            entregable = Entregable(nombre = data.get("nombre"), hoy = data.get("hoy"))
            entregable.save()
        return render(request, "index.html")
    
    else:
        formulario = EntregableFormulario()


    return render(request, "entregable.html", {"formulario": formulario})

def formulario(request):
    
    if request.method == "POST": 
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
        

        curso = Curso(nombre = datos.get("curso"), camada = datos.get("camada"))
        curso.save()

        return render(request, "index.html")
    
    else: 
        formulario = CursoFormulario()

    return render(request, "formulario.html", {"formulario": formulario})