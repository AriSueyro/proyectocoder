from django.contrib import admin

from coderapp.models import Profesor, Estudiante, Curso, Entregable 

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Curso)