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
from .views import eliminar_usuarios,cerrar_sesion,registrarUsuario,EliminarUsuario,EliminarVideoJuego,ModificarJuego,Listado_Videojuegos,Listado_Usuarios,AgregarPCJuego,AgregarPlaystation,AgregarXbox,AgregarNintendo,tienda,registro,olvide_contrasena,Nosotros,inicio_sesion,editarPerfil,Cuenta,Colaboracion,Cambiar_Contrasena,Administracion,Agregar,AgregarN,AgregarP,AgregarPC,AgregarX,Modificar,seccion_playstation,bloodborne,seccion_nintendo,zelda,seccion_Xbox,haloi,seccion_Pc,cyber,carrito,Listado
 


urlpatterns = [
    #Paginas Principales
    path('',tienda,name="tienda"),
    path('registro/',registro,name="registro"),
    path('registrarUsuario',registrarUsuario,name="registrarUsuario" ),
    path('olvide_contrasena/',olvide_contrasena,name="olvide_contrasena"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    path('inicio_sesion/',inicio_sesion,name="inicio_sesion"),
    path('cerrar_sesion/',cerrar_sesion,name="cerrar_sesion"),
    path('eliminar_usuarios/',eliminar_usuarios,name="eliminar_usuarios"),
    path('editar_Perfil/',editarPerfil,name="editarPerfil"),
    path('Cuenta/',Cuenta,name="Cuenta"),
    path('Colaboracion/',Colaboracion,name="Colaboracion"),
    path('Cambiar_Contrasena/',Cambiar_Contrasena,name="Cambiar_Contrasena"),
    
    #Admin
    path('Administracion/',Administracion,name="Administracion"),
    path('Agregar/',Agregar,name="Agregar"),

    path('Agregar/Nintendo/',AgregarN,name="AgregarN"),
    path('AgregarNintendo/',AgregarNintendo,name="AgregarNintendo"),

    path('Agregar/Xbox/',AgregarX,name="AgregarX"),
    path('AgregarXbox/',AgregarXbox,name="AgregarXbox"),

    path('Agregar/Playstation/',AgregarP,name="AgregarP"),
    path('AgregarPlaystation/',AgregarPlaystation,name="AgregarPlaystation"),

    path('Agregar/Steam',AgregarPC,name="AgregarPC"),
    path('AgregarPCJuego/',AgregarPCJuego,name="AgregarPCJuego"),

    path('EliminarVideoJuego/<id>',EliminarVideoJuego,name="EliminarVideoJuego"),
    path('EliminarUsuario/<id>',EliminarUsuario,name="EliminarUsuario"),

    path('Listado/',Listado,name="Listado"),
    path('Listado_Usuarios/',Listado_Usuarios,name="Listado_Usuarios"),
    path('Listado_Videojuegos/',Listado_Videojuegos,name="Listado_Videojuegos"),
    path('Modificar/<id>',Modificar,name="Modificar"),
    path('ModificarJuego',ModificarJuego,name="ModificarJuego"),

    #seccion play
    path('playstation/',seccion_playstation,name="seccion_playstation"),
    path('playstation/bloodborne/',bloodborne,name="bloodborne"),

    #Seccion Xbox
    path('Xbox/',seccion_Xbox,name="seccion_Xbox"),
    path('Xbox/haloInfinite/',haloi,name="haloi"),

    #seccion nintendo 
    path('nintendo/',seccion_nintendo,name="seccion_nintendo"),
    path('nintendo/zelda/',zelda,name="zelda"),

    #Seccion Pc
    path('Steam/',seccion_Pc,name="Seccion_Pc"),
    path('Steam/Cyberpunk/',cyber,name="cyber"),

    #Carrito
    path('Carrito/',carrito,name="Carrito"),

]
