from django.db import models
from django import forms    
from django.contrib.auth.models import User

# Create your models here.

Estado_soli = [
    ('NA', 'No Aprobado'),
    ('A', 'Aprobado'),
]

class RegisterTraveller(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=60, unique=True)
    

class Solicitud(models.Model):
    viajante = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    estado = models.CharField(max_length = 20,choices = Estado_soli, default = 'NA')
    telefono = models.IntegerField(null= False)
    pais = models.CharField(max_length=50, default='')
    ciudad = models.CharField(max_length=50,default='')
    edad = models.IntegerField(null= False )
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')

class Destino(models.Model):
    pais = models.CharField(max_length=20, default='')
    estado = models.CharField(max_length=20, default='')
    domicilio = models.CharField(max_length=20, default='')


    


