"""evaluacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from evalua.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('evalua.urls')), 
     path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    path('logout/', logout_view, name="vista_logout"),
    path('registrar/', registrar_view, name="vista_registro"), 

    path('lista_empresa/', login_required(ListaEmpresa.as_view()), name='listar_empresa'),
    path('crea_empresa/', login_required(CrearEmpresa.as_view()), name='crear_empresa'),
    path('edita_empresa/<int:pk>/', login_required(ActualizarEmpresa.as_view()), name='editar_empresa'),
    path('elimina_empresa/<int:pk>/', login_required(EliminarEmpresa.as_view()), name='eliminar_empresa'),

    path('lista_usuario/', login_required(ListaUsuario.as_view()), name='listar_usuario'),
    path('crea_usuario/', login_required(CrearUsuario.as_view()), name='crear_usuario'),
    path('edita_usuario/<int:pk>/', login_required(ActualizarUsuario.as_view()), name='editar_usuario'),
    path('elimina_usuario/<int:pk>/', login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),

    path('lista_viaje/', login_required(ListaViaje.as_view()), name='listar_viaje'),
    path('crea_viaje/', login_required(CrearViaje.as_view()), name='crear_viaje'),
    path('edita_viaje/<int:pk>/', login_required(ActualizarViaje.as_view()), name='editar_viaje'),
    path('elimina_viaje/<int:pk>/', login_required(EliminarViaje.as_view()), name='eliminar_viaje'),

]
