from django.shortcuts import render
from django.http import HttpResponse

def leer_profesor(request):
    return HttpResponse("vista profesor")
