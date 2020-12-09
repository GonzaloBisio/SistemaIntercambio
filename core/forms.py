from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.mail import EmailMultiAlternatives
from .models import *

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,label='Nombre')
    last_name = forms.CharField(max_length=32, label='Apellido')
    email = forms.EmailField(max_length=60, help_text='Requisito. Añadir email válido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ('username','email','password1','password2','first_name','last_name', )
        help_texts = {k:"" for k in fields}

    
class Solicitud(ModelForm):
    class Meta:
        model = Solicitud
        fields = ( 'telefono', 'ciudad', 'pais','nombre', 'email',)

form = Solicitud()