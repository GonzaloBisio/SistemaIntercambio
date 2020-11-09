from django.db import models
from django import forms    
from django.contrib.auth.models import User

# Create your models here.

ESTADO = [
    ('NR', 'No registrado'),
    ('R', 'Registrado'),
    ('ET', 'En trámite'),
    ('EV', 'Esperando vuelo'),
]

Estado_soli = [
    ('NA', 'No Aprobado'),
    ('A', 'Aprobado'),
]

TRAVEL_CHOICES = ( 
    ("E", "Estudio"), 
    ("C", "Cultural"), 
    ("T", "Trabajo"), 
 
) 

class RegisterTraveller(models.Model):
    codigo = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=ESTADO, default= 'R')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length =50)

class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterTraveller
        fields = ['password1']
        widgets = {'password1': forms.PasswordInput(),}

class RegisterHost(models.Model):
    codigo = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=ESTADO, default= 'R')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length =50)
    disponibilidad = models.IntegerField(default=0)

class Programa(models.Model):
    regist = models.ForeignKey('RegisterTraveller',on_delete=models.CASCADE, null=False)
    opciones = models.CharField( 
        max_length = 20, 
        choices = TRAVEL_CHOICES, 
        default = '-'
        )

class Solicitud(models.Model):
    regist1 = models.ForeignKey('RegisterTraveller',on_delete=models.CASCADE, null=False)
    reg_host = models.ForeignKey('RegisterHost',on_delete=models.CASCADE, null=False)
    estad = models.CharField( 
        max_length = 20, 
        choices = Estado_soli, 
        default = '-'
        )