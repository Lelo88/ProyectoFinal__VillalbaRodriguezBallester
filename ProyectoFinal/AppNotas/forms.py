from django import forms
from django.forms import ModelForm

from .models import Nota

class NotasForm(ModelForm):
    
    class Meta:
        model = Nota
        fields = ['titulo', 'cuerpo', 'etiqueta']
        error_messages = {
			'etiqueta': {
				'required': ("Seleccione una etiqueta, sino, créela."),
			}
		}
        