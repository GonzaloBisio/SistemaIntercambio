from django.db import models
from django import forms    

# Create your models here.

ESTADO = [
    ('NR', 'No registrado'),
    ('R', 'Registrado'),
    ('ET', 'En trámite'),
    ('EV', 'Esperando vuelo'),
]

TRAVEL_CHOICES = ( 
    ("E", "Estudio"), 
    ("C", "Cultural"), 
    ("T", "Trabajo"), 
 
) 

class RegisterTraveller(models.Model):
    codigo = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=ESTADO, default= 'No registrado')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length =50)

class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterTraveller
        fields = ['password']
        widgets = {'password': forms.PasswordInput(),}

class RegisterHost(models.Model):
    codigo = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=ESTADO, default= 'No registrado')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DateField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length =50)

class Programa(models.Model):
    register = models.ForeignKey('RegisterTraveller',on_delete=models.CASCADE, null=False)
    semester = models.CharField( 
        max_length = 20, 
        choices = TRAVEL_CHOICES, 
        default = '-'
        ) 