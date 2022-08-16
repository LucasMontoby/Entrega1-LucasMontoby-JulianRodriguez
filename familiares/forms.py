from django import forms

class BusquedaPersonal(forms.Form):
    apellido = forms.CharField(max_length=30, required=False)