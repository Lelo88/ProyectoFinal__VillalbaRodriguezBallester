from django.urls import path, include

from .views import loginView, registrar

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', registrar, name = 'Registro'),
    path('login/', loginView, name='Login'),
    path('', include('AppNotas.urls')),
    path('logout/',LogoutView.as_view(template_name='padre.html'), name='Logout' )
]