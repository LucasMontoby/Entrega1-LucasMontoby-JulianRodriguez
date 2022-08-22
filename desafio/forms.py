from django import forms

class FormBlog(forms.Form):
    autor = forms.CharField(max_length=30, required=False)
    imagen = forms.ImageField(required=False)
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaBlog(forms.Form):
    autor = forms.CharField(max_length=30, required=False)