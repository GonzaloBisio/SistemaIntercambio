from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserCreationForm, UserChangeForm
from .models import *

# Register your models here.

class RegisterTravellerAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre','apellido','email')
    search_fields = ['nombre','apellido',]
    fieldsets = (
        ("Usuario", {
            'fields': ('usuario',)
        }),
        ("Persona", {
            'fields': ('nombre', 'apellido','email',)
        }),
    )


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('aprobado','perfil','telefono', 'pais','ciudad','nombre','apellido','email','actividad','info',)
    search_fields = ['nombre','apellido','pais']
    list_filter = ('aprobado',)
    fieldsets = (
        ("Aprobacion", {
            'fields': ('aprobado','perfil')
        }),
        ("Persona", {
            'fields': ('nombre', 'apellido','telefono',)
        }),
        ("Contacto", {
            'fields': ('email',)
        }),
        ("Region", {
            'fields': ('pais','ciudad',)
        }),
    )

class DestinyAdmin(admin.ModelAdmin):
    list_display = ('destino', 'ciudad', 'domicilio',)
    fieldsets = (
        ("Region",{
            'fields':('destino', 'ciudad', 'domicilio',)
        }),
    )


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    



admin.site.register(RegisterTraveller, RegisterTravellerAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Destiny, DestinyAdmin)