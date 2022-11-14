from django.urls import path, include

from .views import Inicio

urlpatterns = [
    path('',Inicio.as_view(), name="Inicio"),
    path('', include('AppUsuario.urls'))
]