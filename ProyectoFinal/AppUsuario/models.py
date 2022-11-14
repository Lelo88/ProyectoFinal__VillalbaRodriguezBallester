from django.db import models

# Create your models here.
class Login(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    contraseña = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombre_usuario}'