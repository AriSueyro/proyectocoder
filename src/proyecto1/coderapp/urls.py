from django.contrib import admin
from django.urls import path, include
from coderapp.views import leer_profesor

urlpatterns = [
    path('profesores/', leer_profesor),
]