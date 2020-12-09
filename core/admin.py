from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserCreationForm, UserChangeForm
from .models import *

# Register your models here.

class RegisterTravellerAdmin(admin.ModelAdmin):
    list_display = ('usuario','codigo', 'nombre','apellido','email')
    search_fields = ['nombre','apellido','codigo']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido','email',)
        }),
        ("Codigo", {
            'fields': ('codigo',)
        }),
    )


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('estado','telefono', 'pais','ciudad','nombre','apellido','email','actividad','info',)
    search_fields = ['nombre','apellido','pais']
    fieldsets = (
        ("Aprobacion", {
            'fields': ('estado',)
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

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    


admin.site.register(RegisterTraveller, RegisterTravellerAdmin)
admin.site.register(Solicitud, SolicitudAdmin)