from django.urls import path, include

from .views import Notas

urlpatterns = [
    path('notas/', Notas, name = 'Notas'),
]