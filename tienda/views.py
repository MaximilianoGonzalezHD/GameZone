from django.shortcuts import render,redirect, get_object_or_404
from .models import Compra,Detallesc,Videojuegos,Seccion,Usuario,Rol,Carrito,ItemCarrito
from .serializers import UsuarioSerializer, CompraSerializer, DetallescSerializer, CarritoSerializer, ItemCarritoSerializer,VideojuegosSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate,login, logout 
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, action
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.utils.text import slugify
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
import requests
from datetime import date
import secrets
import string


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
    carrito = None
    items_carrito = []

    if request.user.is_authenticated:
        usuario_id = request.user.id
        usuario = Usuario.objects.get(id_usuariou=usuario_id)
        try:
            carrito = Carrito.objects.get(usuario=usuario)
            items_carrito = ItemCarrito.objects.filter(carrito=carrito)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create(usuario=usuario)
    else:
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)
            items_carrito = ItemCarrito.objects.filter(carrito=carrito)

    contexto = {
        'carrito': carrito,
        'items_carrito': items_carrito
    }

    for item in items_carrito:
        item.subtotal = item.videojuego.precio * item.cantidad

    return render(request, 'tienda/productos/Carrito.html', contexto)

def agregar_producto_al_carrito(request, id, cantidad):
    carrito = None
    usuario = None

    if request.user.is_authenticated:
        usuario_id = request.user.id
        usuario = Usuario.objects.get(id_usuariou=usuario_id)
        try:
            carrito = Carrito.objects.get(usuario=usuario)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create(usuario=usuario)
    else:
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)
        else:
            carrito = Carrito.objects.create(usuario=None)  

            request.session['carrito_id'] = carrito.id_carrito

    if carrito:
        try:
            producto = Videojuegos.objects.get(id_juego=id)
            item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, videojuego=producto, defaults={'cantidad': cantidad})
            if not created:
                item_carrito.cantidad += int(cantidad)
                item_carrito.save()
        except Videojuegos.DoesNotExist:
            return HttpResponse('El producto no existe')
        
        return redirect('Carrito')
    else:
        return HttpResponse('Error al agregar el producto al carrito')

def Comprar_ahora(request, id, cantidad):
    carrito = None
    usuario = None

    if request.user.is_authenticated:
        usuario_id = request.user.id
        usuario = Usuario.objects.get(id_usuariou=usuario_id)
        try:
            carrito = Carrito.objects.get(usuario=usuario)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create(usuario=usuario)
    else:
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)
        else:
            carrito = Carrito.objects.create(usuario=None)  

            request.session['carrito_id'] = carrito.id_carrito

    if carrito:
        try:
            producto = Videojuegos.objects.get(id_juego=id)
            item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, videojuego=producto, defaults={'cantidad': cantidad})
            if not created:
                item_carrito.cantidad += int(cantidad)
                item_carrito.save()
        except Videojuegos.DoesNotExist:
            return HttpResponse('El producto no existe')
        
        return redirect('Pago')
    else:
        return HttpResponse('Error al agregar el producto al carrito')

def borrar_producto_del_carrito(request, id):
    carrito = None
    usuario = request.user

    if usuario.is_authenticated:
        usuario_db = get_object_or_404(Usuario, id_usuariou=usuario.id)
        carrito = get_object_or_404(Carrito, usuario=usuario_db)
    else:
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)

    producto = get_object_or_404(Videojuegos, id_juego=id)

    if carrito:
        ItemCarrito.objects.filter(carrito=carrito, videojuego=producto).delete()
        return redirect('Carrito')
    else:
        return redirect('Carrito')
def limpiar_carrito(request):
    if request.user.is_authenticated:

        usuario_id = request.user.id
        usuario = Usuario.objects.get(id_usuariou=usuario_id)
        carrito = Carrito.objects.get(usuario=usuario)
        carrito.itemcarrito_set.all().delete()
    else:

        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)
            carrito.itemcarrito_set.all().delete()

    return redirect('Carrito')

def buscar_producto(request):
    if request.method == 'GET':
        slug = request.GET.get('query')
        try:
            producto = get_object_or_404(Videojuegos, slug=slug)
            return redirect('mostrar_producto', producto_slug=slug)
        except:
            return redirect('tienda')
    return redirect('tienda')
def pago(request):
    carrito = None
    precio_total = 0
    usuario = None
    correo = None

    if request.user.is_authenticated:
        usuario_id = request.user.id
        usuario = Usuario.objects.get(id_usuariou=usuario_id)
        carrito = Carrito.objects.get(usuario=usuario)
    else:
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = get_object_or_404(Carrito, id_carrito=carrito_id)
        else:
            carrito = Carrito.objects.create(usuario=None)
            request.session['carrito_id'] = carrito.id_carrito

    if carrito:
        items_carrito = ItemCarrito.objects.filter(carrito=carrito)
        for item in items_carrito:
            precio_total += item.videojuego.precio * item.cantidad

    if request.method == 'POST':
        if request.user.is_authenticated:
            rutA = request.POST['rut']

            compra = Compra.objects.create(rutc=rutA, totalc=precio_total, usuario=usuario)
            
            contexto = {
                'usuario': usuario,
                'carrito': carrito,
                'precio_total': precio_total,
                'id_compra': compra
            }

            for item in items_carrito:
                subtotal = item.videojuego.precio * item.cantidad
                Detallesc.objects.create(subtotal=subtotal, cantidad=item.cantidad, videojuego=item.videojuego, compra=compra)

            return redirect('pago_confirmado', id=compra.id_comprac)
        else:
            correo = request.POST['correo']
            rut = request.POST['rut']

            compra = Compra.objects.create(rutc=rut, totalc=precio_total, usuario=None)
            

            contexto = {
                'usuario': usuario,
                'carrito': carrito,
                'precio_total': precio_total,
                'id_compra': compra
            }

            for item in items_carrito:
                subtotal = item.videojuego.precio * item.cantidad
                Detallesc.objects.create(subtotal=subtotal, cantidad=item.cantidad, videojuego=item.videojuego, compra=compra)

            enviar_correo_confirmacion(correo, compra)
            messages.success(request, '¡Compra realizada!')
            items_carrito.delete()
            return redirect('tienda')

    contexto = {
        'usuario': usuario,
        'carrito': carrito,
        'precio_total': precio_total,
    }

    return render(request, 'tienda/inicio/Pago.html', contexto)

def pago_confirmado(request, id):
    compra = Compra.objects.get(id_comprac=id)
    detallesc = Detallesc.objects.filter(compra=compra)
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(8))

    if request.method == 'POST':
        enviar_correo_confirmacion(compra.usuario.emailu, compra)
        messages.success(request, '¡Compra realizada!')

        carrito = Carrito.objects.get(usuario=compra.usuario)
        ItemCarrito.objects.filter(carrito=carrito).delete()

        return redirect('tienda')


    contexto = {
        'compra': compra,
        'detalle': detallesc,
        'codigos':codigo,
    }

    return render(request, 'tienda/inicio/confirmacion_pago.html', contexto)

def enviar_correo_confirmacion(correo, compra):
    id_compra = compra.id_comprac
    fecha_compra = compra.fechac
    total_compra = compra.totalc
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(8))

    mensaje = f"¡Gracias por tu compra!\n\nDetalles de la compra (ID: {id_compra}):\n"
    mensaje += f"Fecha de compra: {fecha_compra}\n"
    mensaje += f"Total de la compra: {total_compra}\n\n"
    mensaje += "Detalles de los productos:\n"

    detallesc = Detallesc.objects.filter(compra=compra)  

    for detalle in detallesc:
        producto = detalle.videojuego
        cantidad = detalle.cantidad
        subtotal = detalle.subtotal

        mensaje += f"- {producto.nombrev} (Cantidad: {cantidad}, Subtotal: {subtotal}, Código de tu producto: {codigo})\n"

    send_mail(
        'Confirmación de compra',
        mensaje,
        'game.zone.pageshop@gmail.com',
        [correo],
        fail_silently=False,
    )
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
@login_required   
def editarPerfil(request, id):
    usuario = Usuario.objects.get(id_usuariou=id)
    rolu = Rol.objects.all()
    contexto ={
        "datos":usuario,
        "datosR":rolu,
    }

    return render(request, 'tienda/inicio/editarPerfil.html',contexto)

@login_required
def modificarcuenta(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('idus')
        correous = request.POST.get('email')
        nombreus = request.POST.get('NombreR')
        nombreopc = request.POST.get('NameOp')
        contrasena = request.POST.get('ContrasenaR')
        imagenus = request.FILES.get('FotoU') 
        rolu = request.POST.get('rolu')

        usuario = Usuario.objects.get(id_usuariou=id_usuario)
        rol1 = Rol.objects.get(id_rolr=rolu)

        user = User.objects.get(username=usuario.nombre_usuariou)
        user.username = nombreus
        user.email = correous
        user.set_password(contrasena)
        user.save()

        if imagenus:
            usuario.imagenu = imagenus
        
        usuario.emailu = correous
        usuario.nombre_usuariou = nombreus
        usuario.nombreu = nombreopc
        usuario.contrasenau = contrasena
        usuario.rol = rol1
        usuario.save()  
       
        return redirect('inicio_sesion')

    return redirect('Cuenta')

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
            return redirect('registro')
        

        try:
            if User.objects.filter(email=emailus).exists():
               mensaje_error = "El correo ya existe"
               return render(request, 'tienda/inicio/registro.html', {'mensaje_error': mensaje_error})
            
            if User.objects.filter(username=nombreuser).exists():
                mensaje_error = "El usuario ya existe"
                return render(request, 'tienda/inicio/registro.html', {'mensaje_error': mensaje_error})
                
            user = User.objects.create_user(email=emailus, username=nombreuser, password=contrau)
            user.is_staff = False
            user.is_active = True
            user.save()
            django_user_id = user.id
            usuario_id = django_user_id
            usuario = Usuario.objects.create(id_usuariou=usuario_id,emailu=emailus, nombre_usuariou=nombreuser,
                                contrasenau=contrau, nombreu=nombreus, rol=registroRol)
            usuario.save()

            

            return redirect('inicio_sesion')
        except IntegrityError:
            return redirect('registro')

    return render(request, 'registro.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuarios(request):
    usuarios = User.objects.all()
    usuarios.delete()
    return HttpResponse("Usuarios eliminados correctamente")

def olvide_contrasena(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'tienda/inicio/olvide_contrasena.html', {'error_message': 'El correo no existe'})

        token, created = Token.objects.get_or_create(user=user)

        reset_url = request.build_absolute_uri(reverse('cambiar_contrasena', args=[user.id, token.key]))

        message = f'Haga clic en el siguiente enlace para restablecer su contraseña: {reset_url}'
        send_mail('Restablecimiento de contraseña', message, 'game.zone.pageshop@gmail.com', [email])

        return redirect('inicio_sesion')

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
            else:
                # Inicio de sesión del usuario normal
                login(request, user)

            # Crear o recuperar el token de autenticación
            token, _ = Token.objects.get_or_create(user=user)

            # Almacenar el token en la sesión del usuario
            request.session['auth_token'] = token.key

            return redirect('tienda')
        else:
            messages.error(request, 'El Email o La contraseña es incorrecto')
            return redirect('inicio_sesion')

    return render(request, 'tienda/inicio/inicio_sesion.html')

def cerrar_sesion(request):
    if request.user.is_authenticated:
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass

    logout(request)
    
    return redirect('inicio_sesion')


@csrf_protect
@login_required
def Cuenta(request):
    usuario = request.user  
    perfil_usuario = Usuario.objects.get(id_usuariou=usuario.id)

    contexto = {
        'usuario': usuario,
        'datos':perfil_usuario,
    }
    return render(request, 'tienda/inicio/Cuenta.html', contexto)

def Colaboracion(request):
    return render(request, 'tienda/inicio/Colaboracion.html')

@require_http_methods(["GET", "POST"])
@csrf_protect
def cambiar_contrasena(request, user_id, token):
    django_user = User.objects.get(id=user_id)
    token_obj = Token.objects.filter(user=django_user).first()
    
    if not token_obj or token != token_obj.key:
        messages.error(request, 'El enlace de restablecimiento de contraseña no es válido')
        return redirect('inicio_sesion')

    if request.method == 'POST':
        password = request.POST.get('NuevaContrasena')

        # Actualizar la contraseña del usuario de Django
        django_user.set_password(password)
        django_user.save()

        # Actualizar la contraseña del usuario en la base de datos
        usuario = Usuario.objects.get(nombre_usuariou=django_user.username)
        usuario.contrasenau = password
        usuario.save()

        messages.success(request, 'La contraseña se ha cambiado exitosamente')
        return redirect('inicio_sesion')

    contexto = {
        'user_id': user_id,
        'token': token, 
    }
    return render(request, 'tienda/inicio/cambiar_contrasena.html', contexto)

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
def EliminarUsuario(request, id):
    usuario = Usuario.objects.get(id_usuariou=id)
    user = User.objects.get(username=usuario.nombre_usuariou)

    # Eliminar el registro de Usuariow
    usuario.delete()

    # Eliminar el usuario de Django
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

#Apis
@permission_classes((IsAuthenticated,))
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
@permission_classes((IsAuthenticated,))
class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
@permission_classes((IsAuthenticated,))
class DetallescViewSet(viewsets.ModelViewSet):
    queryset = Detallesc.objects.all()
    serializer_class = DetallescSerializer
@permission_classes((IsAuthenticated,))
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def obtener_carrito(self, request):
        carrito = Carrito.objects.get(usuario=request.user)
        carrito_serializer = self.get_serializer(carrito)
        return Response(carrito_serializer.data)

    @action(detail=True, methods=['post'])
    def agregar_producto(self, request, pk=None):
        carrito = self.get_object()
        
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad', 1)
        
        try:
            producto = Videojuegos.objects.get(pk=producto_id)

            item_carrito = ItemCarrito.objects.get(carrito=carrito, videojuego=producto)
            
            item_carrito.cantidad += cantidad
            item_carrito.save()
            
            carrito_serializer = self.get_serializer(carrito)
            item_carrito_serializer = ItemCarritoSerializer(item_carrito)

            response_data = {
                'carrito': carrito_serializer.data,
                'item_carrito': item_carrito_serializer.data
            }
            return Response(response_data)
        
        except ItemCarrito.DoesNotExist:
            item_carrito = ItemCarrito(carrito=carrito, videojuego=producto, cantidad=cantidad)
            item_carrito.save()
            
            carrito_serializer = self.get_serializer(carrito)
            item_carrito_serializer = ItemCarritoSerializer(item_carrito)
            
            response_data = {
                'carrito': carrito_serializer.data,
                'item_carrito': item_carrito_serializer.data
            }
            return Response(response_data)
        
@permission_classes((IsAuthenticated,))
class ItemCarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer
@permission_classes((IsAuthenticated,))
class VideojuegosViewSet(viewsets.ModelViewSet):
    queryset = Videojuegos.objects.all()
    serializer_class = VideojuegosSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)