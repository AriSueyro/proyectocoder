from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=100, required=False)
    camada = forms.CharField(max_length=100)

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    hoy = forms.BooleanField()
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=20, required= True)
    email = forms.EmailField(required=True)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)