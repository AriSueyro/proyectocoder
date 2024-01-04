from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=100, required=False)
    camada = forms.CharField(max_length=100)