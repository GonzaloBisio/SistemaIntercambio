from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= "index"),
    path('', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('perfil/', views.perfil, name= 'perfil'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('register/', views.register, name='register'),
]

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)