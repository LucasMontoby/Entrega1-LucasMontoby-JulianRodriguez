from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.Listado1.as_view(), name='listado_1'),
    path('crear_1/', views.Crear1.as_view(), name='crear_1'),
    path('editar_1/<int:pk>/', views.Editar1.as_view(), name='editar_1'),
    path('eliminar_1/<int:pk>/', views.Eliminar1.as_view(), name='eliminar_1'),
    path('mostrar_1/<int:pk>/', views.Mostrar1.as_view(), name='mostrar_1'),
]

