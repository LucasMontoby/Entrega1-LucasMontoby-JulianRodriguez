from django.shortcuts import redirect, render

from .forms import BusquedaBlog, FormBlog
from .models import Blog
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def una_vista(request):
    return render(request, 'base.html', {})

def crear(request):
    if request.method == 'POST':
        form = FormBlog(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            blog = Blog(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_creacion=fecha
            )
            blog.save()

            return redirect('listado')
        
        else:
            return render(request, 'blog/crear.html', {'form': form})
            
    
    form_blog = FormBlog()
    
    return render(request, 'crear.html', {'form': form_blog})


def listado(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado = Blog.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listado = Blog.objects.all()
    
    form = BusquedaBlog()
    return render(request, 'blog/listado.html', {'listado': listado, 'form': form})

# @login_required
def editar(request, id):
    blog= Blog.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormBlog(request.POST)       
        if form.is_valid():
            blog.nombre = form.cleaned_data.get('nombre')
            blog.edad = form.cleaned_data.get('edad')
            blog.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            blog.save()

            return redirect('listado')
        
        else:
            return render(request, 'blog/editar.html', {'form': form, 'blog': blog})
    
    form_blog = FormBlog(initial={'nombre': blog.nombre, 'edad': blog.edad, 'fecha_creacion': blog.fecha_creacion })
    
    return render(request, 'blog/editar.html', {'form': form_blog, 'blog': blog})

@login_required
def eliminar(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    
    return redirect('listado')

def mostrar(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/mostrar.html', {'blog': blog})

def about(request):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/about.html', {'blog': blog})