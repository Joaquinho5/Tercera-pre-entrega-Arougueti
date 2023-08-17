from django import forms

class JugadorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    posicion = forms.IntegerField(required=True)

class TecnicoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    estilo = forms.CharField(required=True)

class FormacionForm(forms.Form):
    formacio = forms.CharField(max_length=50, required=True)
    tactica = forms.CharField(max_length=50, required=True)