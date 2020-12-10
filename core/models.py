from django.db import models
from django import forms    
from django.contrib.auth.models import User

# Create your models here.


class RegisterTraveller(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return self.usuario.username
    
class Solicitud(models.Model):
    perfil = models.ForeignKey(RegisterTraveller, on_delete=models.CASCADE, null=True)
    aprobado = models.BooleanField(default= 0)
    telefono = models.IntegerField(null= False )
    pais = models.CharField(max_length=50, default='')
    ciudad = models.CharField(max_length=50,default='')
    nombre = models.CharField(max_length=50, default='', null=False)
    apellido = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=60, unique=False, default='')
    info = models.CharField(max_length=50,default='')
    actividad = models.CharField(max_length=50,default='')
    
    
class Destiny(models.Model):
    destino = models.CharField(max_length=50,default='')
    ciudad = models.CharField(max_length=50,default='')
    domicilio = models.CharField(max_length=50,default='')


class Actividad(models.Model):
    actividad = models.CharField(max_length=50,default='')
