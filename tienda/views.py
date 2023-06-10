from django.shortcuts import render,redirect, get_object_or_404
from .models import Compra,Detallesc,Videojuegos,Seccion,Usuario,Rol
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.utils.text import slugify


# Create your views here.
#Paginas Principales
def tienda(request):
    return render(request,'tienda/inicio/tienda.html')

#Secciones
def seccion_playstation(request):
    productos_playstation = Videojuegos.objects.filter(seccion = 2)

    contexto = {
        "producto_playstation": productos_playstation
    }
    return render(request,'tienda/productos/Seccion_Play/seccion_playstation.html',contexto)

def seccion_Xbox(request):
    productos_xbox = Videojuegos.objects.filter(seccion = 3)

    contexto = {
        "producto": productos_xbox
    }
    return render(request,'tienda/productos/Seccion_Xbox/seccion_xbox.html',contexto)

def seccion_nintendo(request):
    productos_nintendo = Videojuegos.objects.filter(seccion = 1)

    contexto = {
        "producto": productos_nintendo
    }
    return render(request,'tienda/productos/SeccionNintendo/seccion_nintendo.html',contexto)

def seccion_Pc(request):
    productos_pc = Videojuegos.objects.filter(seccion = 4)

    contexto = {
        "producto": productos_pc
    }
    return render(request,'tienda/productos/SeccionPc/Seccion_Pc.html',contexto)

def carrito(request):
    return render(request,'tienda/productos/carrito.html')

#Productos
def mostrar_producto(request, producto_slug):
    producto = get_object_or_404(Videojuegos, slug=producto_slug)

    if producto.seccion.nombres == 'Playstation':
        return render(request, 'tienda/productos/Seccion_Play/productoPlaystation.html', {'producto': producto})
    elif producto.seccion.nombres == 'Xbox':
        return render(request, 'tienda/productos/Seccion_Xbox/productoXbox.html', {'producto': producto})
    elif producto.seccion.nombres == 'Nintendo':
        return render(request, 'tienda/productos/SeccionNintendo/productoNintendo.html', {'producto': producto})
    elif producto.seccion.nombres == 'Pc':
        return render(request, 'tienda/productos/SeccionPc/productoPc.html', {'producto': producto})
    else:
        return redirect('tienda') 




#Paginas iniciales
def registro(request):
    return render(request, 'tienda/inicio/registro.html')
def registrarUsuario(request):
    if request.method == 'POST':
        emailus = request.POST['email']
        nombreuser = request.POST['NombreR']
        contrau = request.POST['ContrasenaR']
        nombreus = request.POST['NameOp']
        rolu = request.POST['rolu']

        try:
            registroRol = Rol.objects.get(id_rolr=rolu)
        except Rol.DoesNotExist:
            messages.error(request, 'El rol seleccionado no existe')
            return redirect('registro')

        try:
            if User.objects.filter(email=emailus).exists():
                messages.error(request, 'Ya existe un usuario con ese correo electrónico')
                return redirect('registro')

            usuario = Usuario.objects.create(emailu=emailus, nombre_usuariou=nombreuser,
                                            contrasenau=contrau, nombreu=nombreus, rol=registroRol)
            usuario.save()

            user = User.objects.create_user(email=emailus, username=nombreuser, password=contrau)
            user.is_staff = False
            user.is_active = True
            user.save()

            return redirect('inicio_sesion')
        except IntegrityError:
            messages.error(request, 'Error al crear el usuario')
            return redirect('registro')

    return render(request, 'registro.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuarios(request):
    usuarios = User.objects.all()
    usuarios.delete()
    return HttpResponse("Usuarios eliminados correctamente")
@login_required
def olvide_contrasena(request):
    return render(request, 'tienda/inicio/olvide_contrasena.html')

def Nosotros(request):
    return render(request, 'tienda/inicio/Nosotros.html')

def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('emaili')
        contrasena = request.POST.get('contrasenaI')

        # Autenticación del usuario
        user = authenticate(request, email=email, password=contrasena)

        if user is not None:
            if user.is_superuser:
                # Inicio de sesión del superusuario
                login(request, user)
                return redirect('tienda')
            else:
                # Inicio de sesión del usuario normal
                login(request, user)
                return redirect('tienda')
        else:
            messages.error(request, 'El Email o La contraseña es incorrecto')
            return redirect('inicio_sesion')

    return render(request, 'tienda/inicio/inicio_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion')
@login_required   
def editarPerfil(request):
    return render(request, 'tienda/inicio/editarPerfil.html')
@login_required
def Cuenta(request):
    return render(request, 'tienda/inicio/Cuenta.html')

def Colaboracion(request):
    return render(request, 'tienda/inicio/Colaboracion.html')
@login_required
def Cambiar_Contrasena(request):
    return render(request, 'tienda/inicio/Cambiar_Contrasena.html')

#Paginas Administrativas
@login_required
@user_passes_test(lambda u: u.is_superuser)
def Administracion(request):
    return render(request, 'tienda/admin/Administracion.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)
def Agregar(request):
    return render(request, 'tienda/admin/Agregar.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)
def Listado(request):
    return render(request, 'tienda/admin/Listado.html')

#Seccion agregar
@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarN(request):
    nin = 1
    contexto = {
        "Nintendo": nin
    }
    return render(request, 'tienda/admin/Secciones/AgregarN.html',contexto)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarNintendo(request):
    nombreN = request.POST['NameGameN']
    descripcionN = request.POST['DescripcionN']
    precioN = request.POST['PrecioN']
    imagenN = request.FILES['FotoVN']
    seccionN = request.POST['SeccionVN']
    
    registroSeccionN = Seccion.objects.get(id_seccions = seccionN)

    videojuego = Videojuegos.objects.create(nombrev = nombreN, descripcion = descripcionN,
                               precio = precioN, imagenv = imagenN, seccion = registroSeccionN)
    
    videojuego.slug = slugify(videojuego.nombrev)
    videojuego.save()
    return redirect(AgregarN)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarP(request):
    Play = 2
    contexto = {
        "Playstation": Play
    }
    return render(request, 'tienda/admin/Secciones/AgregarP.html', contexto)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarPlaystation(request):
    nombreP = request.POST['NameGameP']
    descripcionP = request.POST['DescripcionP']
    precioP = request.POST['PrecioP']
    imagenP = request.FILES['fotoP']
    seccionP = request.POST['SeccionVP']
    
    registroSeccionP = Seccion.objects.get(id_seccions = seccionP)

    videojuego = Videojuegos.objects.create(nombrev = nombreP, descripcion = descripcionP,
                               precio = precioP, imagenv = imagenP, seccion = registroSeccionP)

    videojuego.slug = slugify(videojuego.nombrev)
    videojuego.save()
    return redirect(AgregarP)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarPC(request):
    Compu = 4
    contexto = {
        "PC": Compu
    }
    return render(request, 'tienda/admin/Secciones/AgregarPC.html',contexto)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarPCJuego(request):
    nombrePC = request.POST.get('NombrePc')
    descripcionPC = request.POST.get('DescripcionPc')
    precioPC = request.POST.get('PrecioPc')
    imagenPC = request.FILES.get('FotoPc')
    seccionPC = request.POST.get('SeccionVPC')
    
    registroSeccionPC = Seccion.objects.get(id_seccions = seccionPC)

    videojuego = Videojuegos.objects.create(nombrev = nombrePC, descripcion = descripcionPC,
                               precio = precioPC, imagenv = imagenPC, seccion = registroSeccionPC)
    videojuego.slug = slugify(videojuego.nombrev)
    videojuego.save()
    return redirect(AgregarPC)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarX(request):
    Xbo = 3
    contexto = {
        "Xbox": Xbo
    }
    return render(request, 'tienda/admin/Secciones/AgregarX.html',contexto)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AgregarXbox(request):
    nombreX = request.POST['NameGameX']
    descripcionX = request.POST['DescripcionX']
    precioX = request.POST['PrecioX']
    imagenX = request.FILES['FotoX']
    seccionX = request.POST['SeccionVX']
    
    registroSeccionX = Seccion.objects.get(id_seccions = seccionX)

    videojuego = Videojuegos.objects.create(nombrev = nombreX, descripcion = descripcionX,
                               precio = precioX, imagenv = imagenX, seccion = registroSeccionX)
    
    videojuego.slug = slugify(videojuego.nombrev)
    videojuego.save()
    return redirect(AgregarX)

#Modificar Usuarios
@login_required
@user_passes_test(lambda u: u.is_superuser)
def Listado_Usuarios(request):
    listado = Usuario.objects.all()
    contexto = {
        "listadoUsuarios":listado
    }

    return render(request, 'tienda/admin/Listado_Usuarios.html',contexto)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def EliminarUsuario(request,id):
    user = Usuario.objects.get(id_usuariou = id)
    user.delete()
    return redirect('Listado_Usuarios')

#modificar Productos
@login_required
@user_passes_test(lambda u: u.is_superuser)
def Modificar(request, id):
    Videojuego = Videojuegos.objects.get(id_juego = id)
    listado = Seccion.objects.all()
    contexto = {
        "datos": Videojuego,
        "ListadoS": listado
    }
    return render(request, 'tienda/admin/Modificar.html',contexto)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def ModificarJuego(request):
    if request.method == 'POST':
        v_id = request.POST.get('IDV')
        nombrev = request.POST.get('NameGameV')
        descripcionv = request.POST.get('DescripcionV')
        preciov = request.POST.get('PrecioV')
        imagenvid = request.FILES.get('FotoV')
        seccionv2 = request.POST.get('seccionV')

        videojuego = Videojuegos.objects.get(id_juego=v_id)
        seccionvi = Seccion.objects.get(id_seccions=seccionv2)
        videojuego.nombrev = nombrev
        videojuego.descripcion = descripcionv
        videojuego.precio = preciov

        if imagenvid:
            videojuego.imagenv = imagenvid

        videojuego.seccion = seccionvi

        videojuego.save()
        return redirect('Listado_Videojuegos')

    return HttpResponse('Método no permitido')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def Listado_Videojuegos(request):
    listado = Videojuegos.objects.all()
    contexto = {
        "listadoVideojuegos":listado
    }
    return render(request, 'tienda/admin/Listado_Videojuegos.html',contexto)

#Eliminar VideoJuegos
@login_required
@user_passes_test(lambda u: u.is_superuser)
def EliminarVideoJuego(request,id):
    videojuego = Videojuegos.objects.get(id_juego = id)
    videojuego.delete()
    return redirect('Listado_Videojuegos')



