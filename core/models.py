from django.db import models
from django import forms    

# Create your models here.


class RegisterTraveller(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length =50)

class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterTraveller
        fields = ['password']
        widgets = {'password': forms.PasswordInput(),}
