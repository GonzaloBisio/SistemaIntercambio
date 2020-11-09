from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def index (request):
    return render (request, "core/index.html")

def login (request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nombre']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
        else: 
            form = UserCreationForm()

            
        if request.POST.get("Viaje")=="2":
            RegisterHost.objects.create()
        else:
            RegisterTraveller.objects.create(nombre=request.POST.get(name))

    return render (request, "core/login.html")

def register (request):
    return render (request, "core/register.html")
    
def perfil (request):
    perf = RegisterTraveller.objects.all()
    return render (request, "core/perfil.html",{'perf': perf})

