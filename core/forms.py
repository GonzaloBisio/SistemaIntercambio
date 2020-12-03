from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives

from core.models import RegisterTraveller

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Requisito. Añadir email válido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Contraseña', widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

    