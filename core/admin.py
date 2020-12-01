from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserCreationForm, UserChangeForm
from .models import *

# Register your models here.

class RegisterTravellerAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'apellido','status',)
    search_fields = ['nombre','apellido','codigo']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido','edad','password1','email',)
        }),
        ("Codigo", {
            'fields': ('codigo',)
        }),
        ("Region", {
            'fields': ('pais','estado',)
        }),
    )

class RegisterHostAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'apellido','status','disponibilidad','pais','estado',)
    search_fields = ['nombre','apellido','codigo']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido','edad','password','email',)
        }),
        ("Codigo", {
            'fields': ('codigo',)
        }),
        ("Region", {
            'fields': ('pais','estado',)
        }),
        ("Disponibilidad", {
            'fields': ('disponibilidad',)
        }),
    )

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    


admin.site.register(RegisterTraveller,RegisterTravellerAdmin)
admin.site.register(RegisterHost,RegisterHostAdmin) 
admin.site.register(Programa) 
admin.site.register(Solicitud)
admin.site.register(Profile)
