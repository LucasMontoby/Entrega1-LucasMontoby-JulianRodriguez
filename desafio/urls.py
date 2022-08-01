from django.urls import path
from .views import una_vista, crear, listado, editar, eliminar, mostrar
from .views import about

urlpatterns = [
    path('', una_vista, name='base'), 
    path('about/', about, name='about'),
    path('blog/', listado, name='listado'),
    path('crear/', crear, name='crear'),
    path('editar/<int:id>/', editar, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('mostrar/<int:id>/', mostrar, name='mostrar'),
]