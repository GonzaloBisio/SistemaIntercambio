from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Solicitud as SoliModel
from .models import RegisterTraveller as Regi
from .forms import UserRegisterForm
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index (request):
    perf = request.user
    nom = RegisterTraveller.objects.get(usuario = perf)
    if request.method == "POST":
        if "pais" in request.POST:
            nombre = request.POST["name"]
            noms = request.POST["nombre"]
            apell = request.POST["apellido"]
            email = request.POST["eaddress"]
            telefono = request.POST["phone"]
            ciudad = request.POST["city"]
            info = request.POST["info"]
            actividad = request.POST["actividad"]
            pais = request.POST["pais"]
            subject = "Solicitud Viaje"
            message = "El nombre es: " + nombre +"\n"+ "El pais: " + pais + "\n" + "La info: " + info
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["dreamtripgt@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
            print (nombre)
            obj_perf = User.objects.get(username = nombre)
            obj_reg = RegisterTraveller.objects.get(usuario =obj_perf )
            ins = SoliModel.objects.create(perfil= obj_reg ,nombre=noms,apellido=apell,pais=pais,actividad=actividad, email=email,telefono=telefono ,ciudad=ciudad ,info=info  )
            ins.save()
            print("datos cargados")

        else:
            nombre = request.POST.get("contact_name")
            mail = request.POST.get("contact_email")
            mensaj = request.POST.get("contact_message")
            subject = "Contacto"
            message = "El nombre es: " + nombre +"\n"+ "El mensaje es: " + mensaj
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["dreamtripgt@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
            
    return render (request, "core/index.html", {'perf': perf , 'nom': nom, })

def login (request):
    messages.success(request, f'Te has deslogeado... Adios {username} ')
    return render (request, "core/login.html")

def register (request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            nombre = request.POST["first_name"]
            apellido = request.POST["last_name"]
            email = request.POST["email"]
            form.save()
            username = form.cleaned_data['username']
            inst = Regi.objects.create(usuario=User.objects.get(username = usuario) ,nombre=nombre, email=email, apellido=apellido )
            inst.save()
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
        else:
            messages.warning(request, f'Ingresaste mal tu contraseña')
            return redirect('register')
    else:
            form = UserRegisterForm()
    context = {'form' : form}
    return render (request, "core/register.html", context )

@login_required(login_url='login')   
def perfil (request):
    perf = request.user
    nom = RegisterTraveller.objects.get(usuario = perf)
    solis = Solicitud.objects.filter(perfil= nom) 
    return render (request, "core/perfil.html",{'perf': perf , 'solis': solis, 'nom': nom})

@login_required(login_url='login')   
def solicitud (request):
    perf = request.user
    nom = RegisterTraveller.objects.get(usuario = perf)
    paises = Destiny.objects.all()
    act = Actividad.objects.all()
    return render (request, "core/solicitud.html", {'perf': perf , 'nom': nom , 'paises': paises, 'act': act})

