from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaPersonal

from .models import Personal


class Listado1(ListView):
    model=Personal
    template_name = 'personal/listado_1.html'
    
    def get_queryset(self):
        apellido = self.request.GET.get('apellido', '')
        if apellido:
            object_list = self.model.objects.filter(apellido__icontains=apellido)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPersonal()
        return context
    
class Crear1(CreateView):
    model=Personal
    template_name = 'personal/crear_1.html'
    success_url = '/familiares/personal'
    fields = ['apellido', 'edad', 'fecha_creacion']


class Editar1(LoginRequiredMixin, UpdateView):
    model=Personal
    template_name = 'personal/editar_1.html'
    success_url = '/familiares/personal'
    fields = ['apellido', 'edad', 'fecha_creacion']


class Eliminar1(LoginRequiredMixin, DeleteView):
    model=Personal
    template_name = 'personal/eliminar_1.html'
    success_url = '/familiares/personal'


class Mostrar1(DetailView):
    model = Personal
    template_name='personal/mostrar_1.html'
    