from django.urls import path, include

from .views import Inicio, Presentacion

urlpatterns = [
    path('',Inicio.as_view(), name="Inicio"),
    path('inicio/', Presentacion.as_view(), name="Presentacion"),
    path('', include('AppUsuario.urls')),
]