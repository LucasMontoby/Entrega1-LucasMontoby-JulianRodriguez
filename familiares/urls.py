from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.Listado.as_view(), name='listado_1'),
    path('crear-1/', views.Crear1.as_view(), name='crear_1'),
    path('editar-1/<int:pk>/', views.Editar1.as_view(), name='editar_1'),
    path('eliminar-1/<int:pk>/', views.Eliminar1.as_view(), name='eliminar_1'),
    path('mostrar-1/<int:pk>/', views.Mostrar1.as_view(), name='mostrar_1'),
]

