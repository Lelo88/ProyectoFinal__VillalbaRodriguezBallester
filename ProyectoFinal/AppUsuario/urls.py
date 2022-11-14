from django.urls import path, include

from .views import loginView, registrar

urlpatterns = [
    path('registro/', registrar, name = 'Registro'),
    path('login/', loginView, name='Login'),
    path('', include('AppNotas.urls'))
]