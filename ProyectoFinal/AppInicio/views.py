from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Inicio(TemplateView):
    template_name = 'padre.html'

class Presentacion(TemplateView):
    template_name = 'inicio.html'
    messages = 'Hola'