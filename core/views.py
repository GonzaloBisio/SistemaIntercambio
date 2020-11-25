from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def index (request):
    return render (request, "core/index.html")

def login (request):
    return render (request, "core/login.html")

def register (request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
            form = UserRegisterForm()
    context = {'form' : form}
    return render (request, "core/register.html", context)
    
def perfil (request):
    perf = RegisterTraveller.objects.all()
    return render (request, "core/perfil.html",{'perf': perf})

def solicitud(request):
    return render (request, "core/solicitud.html")

