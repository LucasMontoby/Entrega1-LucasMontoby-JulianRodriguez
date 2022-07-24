from django import forms

class FormBlog(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaBlog(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)