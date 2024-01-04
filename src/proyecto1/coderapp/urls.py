from django.contrib import admin
from django.urls import path, include
from coderapp.views import leer_profesor, leer_alumnos, index, profesor, estudiante, curso, entregable, formulario

urlpatterns = [
    path("", index, name = 'index'),
    path("profesores/", profesor, name = 'profesor'),
    path("estudiantes/", estudiante, name = 'estudiante'),
    path("curso/", curso, name = 'curso'),
    path("entregable/", entregable, name = 'entregable'),
    path("formulario/", formulario, name = 'formulario'),
]