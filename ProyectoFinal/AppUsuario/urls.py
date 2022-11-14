from django.urls import path

from .views import loginView, registrar

urlpatterns = [
    path('registro/', registrar, name = 'Registro'),
    path('login/', loginView, name='Login')
]