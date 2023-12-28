from django.contrib import admin
from django.urls import path, include
from coderapp.views import leer_profesor, leer_alumnos, index, profesor, estudiante, curso, entregable

urlpatterns = [
    path('profesores/', leer_profesor),
    path("alumnos/", leer_alumnos),
    path("", index),
    path("profesor/", profesor),
    path("estudiante/", estudiante),
    path("curso/", curso),
    path("entregable/", entregable),
]