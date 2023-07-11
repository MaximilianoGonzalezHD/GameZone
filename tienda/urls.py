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
from .views import historial_compras,modificarcontrasena,editarContrasena,buscar_producto,Comprar_ahora,pago_confirmado,pago,limpiar_carrito,borrar_producto_del_carrito,agregar_producto_al_carrito,modificarcuenta,mostrar_producto,eliminar_usuarios,cerrar_sesion,registrarUsuario,EliminarUsuario,EliminarVideoJuego,ModificarJuego,Listado_Videojuegos,Listado_Usuarios,AgregarPCJuego,AgregarPlaystation,AgregarXbox,AgregarNintendo,tienda,registro,olvide_contrasena,Nosotros,inicio_sesion,editarPerfil,Cuenta,Colaboracion,cambiar_contrasena,Administracion,Agregar,AgregarN,AgregarP,AgregarPC,AgregarX,Modificar,seccion_playstation,seccion_nintendo,seccion_Xbox,seccion_Pc,carrito,Listado
from rest_framework import routers


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
    path('editar_Perfil/<int:id>',editarPerfil,name="editarPerfil"),
    path('editar_contrasena/<int:id>',editarContrasena,name="editarContrasena"),
    path('Cuenta/',Cuenta,name="Cuenta"),
    path('Colaboracion/',Colaboracion,name="Colaboracion"),
    path('cambiar_contrasena/<int:user_id>/<str:token>/',cambiar_contrasena,name="cambiar_contrasena"),
    path('modificarcuenta',modificarcuenta,name="modificarcuenta"),
    path('modificarcontrasena',modificarcontrasena,name="modificarcontrasena"),
        
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
    path('agregar_al_carrito/<int:id>/<int:cantidad>/', agregar_producto_al_carrito, name='agregar_al_carrito'),
    path('Comprar_ahora/<int:id>/<int:cantidad>/', Comprar_ahora, name='Comprar_ahora'),
    path('carrito/borrar/<int:id>/', borrar_producto_del_carrito, name='borrar_producto_del_carrito'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),
    path('Pago/', pago, name='Pago'),
    path('pago-confirmado/<int:id>/', pago_confirmado, name='pago_confirmado'),

    path('buscar/', buscar_producto, name='buscar_producto'),

    #seccion play
    path('playstation/',seccion_playstation,name="seccion_playstation"),
    
    #Seccion Xbox
    path('Xbox/',seccion_Xbox,name="seccion_Xbox"),

    #seccion nintendo 
    path('nintendo/',seccion_nintendo,name="seccion_nintendo"),

    #Seccion Pc
    path('Steam/',seccion_Pc,name="Seccion_Pc"),


    #Carrito
    path('Carrito/',carrito,name="Carrito"),
    
    #Historial_Compras
    path('historial_compras/',historial_compras, name="historial_compras"),

    #Productos
    path('producto/<slug:producto_slug>/',mostrar_producto,name='mostrar_producto'),

]
