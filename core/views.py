from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from .forms import UserRegisterForm
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.


def index (request):
    if request.method == "POST":
        if "pais" in request.POST:
            nombre = request.POST.get("name")
            info = request.POST.get("info")
            pais = request.POST.get("pais")
            subject = "Solicitud Viaje"
            message = "El nombre es: " + nombre +"\n"+ "El pais: " + pais + "\n" + "La info: " + info
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["dreamtripgt@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
        else:
            nombre = request.POST.get("contact_name")
            mail = request.POST.get("contact_email")
            mensaj = request.POST.get("contact_message")
            subject = "Contacto"
            message = "El nombre es: " + nombre +"\n"+ "El mensaje es: " + mensaj
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["dreamtripgt@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
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
            
            return redirect('login')
    else:
            form = UserRegisterForm()
    context = {'form' : form}
    return render (request, "core/register.html", context)
    
def perfil (request):
    perf = RegisterTraveller.objects.all()
    return render (request, "core/perfil.html",{'perf': perf})

def solicitud (request):
    return render (request, "core/solicitud.html")


def logout(request):
    auth.logout(request)
    return redirect('login')     