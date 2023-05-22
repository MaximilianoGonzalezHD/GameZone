"""GameZone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views 
import tienda,registro,olvide_contrasena,Nosotros,inicio_sesion,editarPerfil,Cuenta,Colaboracion,Cambiar_Contrasena,
 Administracion,agregar,AgregarN,AgregarP,AgregarPC,AgregarX,Eliminar,Modificar
 seccion_playstation,bloodborne,
 seccion_nintendo,zelda,
 seccion_Xbox,haloi,
 Seccion_Pc,cyber,
 


urlpatterns = [
    #Paginas Principales
    path('',tienda,name="tienda"),
    path('registro/',registro,name="registro")
    path('olvide_contrasena/',olvide_contrasena,name="olvide_contrasena")
    path('Nosotros/',Nosotros,name="Nosotros")
    path('inicio_sesion/',inicio_sesion,name="inicio-sesion")
    path('editar_Perfil/',editarPerfil,name="editarPerfil")
    path('Cuenta/',Cuenta,name="Cuenta")
    path('Colaboracion/',Colaboracion,name="Colaboracion")
    path('Cambiar_Contrasena/',Cambiar_Contrasena,name="Cambiar_Contrasena")
    
    #Admin
    path('Administracion/',Administracion,name="Administracion")
    path('Agregar/',Agregar,name="Agregar")
    path('Agregar/Nintendo/',AgregarN,name="AgregarN")
    path('Agregar/Xbox/',AgregarX,name="AgregarX")
    path('Agregar/Playstation/',AgregarP,name="AgregarP")
    path('Agregar/Steam',AgregarPC,name="AgregarPC")
    path('Eliminar/',Eliminar,name="Eliminar")
    path('Modificar/',Modificar,name="Modificar")


    #seccion play
    path('playstation/',seccion_playstation,name="seccion_playstation"),
    path('playstation/bloodborne/',bloodborne,name="bloodborne"),

    #Seccion Xbox
    path('Xbox/',seccion_Xbox,name="seccion_Xbox")
    path('Xbox/haloInfinite/',haloi,name="haloi")

    #seccion nintendo 
    path('nintendo/',seccion_nintendo,name="seccion_nintendo"),
    path('nintendo/zelda/',zelda,name="zelda"),

    #Seccion Pc
    path('Steam/',Seccion_Pc,name="Seccion_Pc")
    path('Steam/Cyberpunk/',cyber,name="cyber")

    #Carrito
    path('Carrito/',Carrito,name="Carrito")

]
