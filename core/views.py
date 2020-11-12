from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def index (request):
    return render (request, "core/index.html")

def login (request):
    return render (request, "core/login.html")

def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaid():
            username = form.clean_data['username']
            messages.sucess(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render (request, "core/register.html")
    
def perfil (request):
    perf = RegisterTraveller.objects.all()
    return render (request, "core/perfil.html",{'perf': perf})

