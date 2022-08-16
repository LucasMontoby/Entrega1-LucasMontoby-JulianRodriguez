from django import forms

class FormBlog(forms.Form):
    autor = forms.CharField(max_length=30)
    imagen = forms.ImageField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaBlog(forms.Form):
    autor = forms.CharField(max_length=30, required=False)