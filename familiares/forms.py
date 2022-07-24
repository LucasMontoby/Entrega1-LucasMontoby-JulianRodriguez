from django import forms

class Busqueda(forms.Form):
    apodo = forms.CharField(max_length=30, required=False)