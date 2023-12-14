from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarReservas, name='reservas'),
    path('detalle/<str:pk>',views.FiltrarReserva, name='detalle'),
    path('crear', views.CrearReserva, name="crear"),
    path('actualizar/<str:pk>/', views.ActualizarReserva, name="actualizar"),
    path('eliminar/<str:pk>/', views.EliminarReserva, name="eliminar"),
    ]