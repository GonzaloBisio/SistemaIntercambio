from django.db import models
from django import forms    
from django.contrib.auth.models import User

# Create your models here.

Estado_solic = [
    ('NA', 'No Aprobado'),
    ('A', 'Aprobado'),
]

Activity = [
    ('I', 'Idiomas'),
    ('F', 'Financias'),
    ('M', 'Musica'),
    ('T', 'Turismo'),
    ('G', 'Guia'),
]

class RegisterTraveller(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=60, unique=True)
    
class Solicitud(models.Model):
    estado = models.CharField(max_length=50, choices=Estado_solic, default='NA')
    actividad = models.CharField(max_length=50, choices=Activity, default='T')
    telefono = models.IntegerField(null= False )
    pais = models.CharField(max_length=50, default='')
    ciudad = models.CharField(max_length=50,default='')
    nombre = models.CharField(max_length=50, default='', null=False)
    apellido = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=60, unique=True, default='')
    actividad = models.CharField(max_length=50,default='')
    info = models.CharField(max_length=50,default='')

class Destino(models.Model):
    pais = models.CharField(max_length=20, default='')
    estado = models.CharField(max_length=20, default='')
    domicilio = models.CharField(max_length=20, default='')


    


