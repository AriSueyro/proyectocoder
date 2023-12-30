from django.contrib import admin
from django.urls import path, include
from coderapp.views import leer_profesor, leer_alumnos, index, profesor, estudiante, curso, entregable

urlpatterns = [
    path('profesores/', leer_profesor),
    path("alumnos/", leer_alumnos),
    path("", index, name = 'index'),
    path("profesor/", profesor, name = 'profesor'),
    path("estudiante/", estudiante, name = 'estudiante'),
    path("curso/", curso, name = 'curso'),
    path("entregable/", entregable, name = 'entregable'),
]