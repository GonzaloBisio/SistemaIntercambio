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



class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    


admin.site.register(RegisterTraveller,RegisterTravellerAdmin)
admin.site.register(Solicitud)
admin.site.register(Profile)
