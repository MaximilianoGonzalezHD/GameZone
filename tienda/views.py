from django.shortcuts import render, redirect
from .models import Compra,Detallesc,Videojuegos,Seccion,Usuario,Rol
# Create your views here.
#Paginas Principales
def tienda(request):
    return render(request,'tienda/inicio/tienda.html')

#Secciones
def seccion_playstation(request):
    return render(request,'tienda/productos/Seccion_Play/seccion_playstation.html')

def seccion_Xbox(request):
    return render(request,'tienda/productos/Seccion_Xbox/seccion_xbox.html')

def seccion_nintendo(request):
    return render(request,'tienda/productos/SeccionNintendo/seccion_nintendo.html')

def seccion_Pc(request):
    return render(request,'tienda/productos/SeccionPc/Seccion_Pc.html')

def carrito(request):
    return render(request,'tienda/productos/carrito.html')

#productos play
def bloodborne(request):
    return render(request,'tienda/productos/Seccion_Play/bloodborne.html')
#Productos Xbox
def haloi(request):
    return render(request,'tienda/productos/Seccion_Xbox/haloi.html')
#Productos nintendo
def zelda(request):
    return render(request,'tienda/productos/SeccionNintendo/zelda.html')
#Productos PC
def cyber(request):
    return render(request,'tienda/productos/SeccionPc/cyber.html')




#Paginas iniciales
def registro(request):
    return render(request, 'tienda/inicio/registro.html')
def registrarUsuario(request):
    emailus = request.POST['email']
    nombreuser = request.POST['NombreR']
    contrau = request.POST['ContrasenaR']
    nombreus = request.POST['NameOp']
    rolu = request.POST['rolu']

    registroRol = Rol.objects.get(id_rolr = rolu)

    Usuario.objects.create(emailu = emailus, nombre_usuariou = nombreuser,
                           contrasenau = contrau, nombreu = nombreus, rol = registroRol )
    return redirect('inicio_sesion')

def olvide_contrasena(request):
    return render(request, 'tienda/inicio/olvide_contrasena.html')

def Nosotros(request):
    return render(request, 'tienda/inicio/Nosotros.html')

def inicio_sesion(request):
    return render(request, 'tienda/inicio/inicio_sesion.html')

def editarPerfil(request):
    return render(request, 'tienda/inicio/editarPerfil.html')

def Cuenta(request):
    return render(request, 'tienda/inicio/Cuenta.html')

def Colaboracion(request):
    return render(request, 'tienda/inicio/Colaboracion.html')

def Cambiar_Contrasena(request):
    return render(request, 'tienda/inicio/Cambiar_Contrasena.html')

#Paginas Administrativas
def Administracion(request):
    return render(request, 'tienda/admin/Administracion.html')
def Agregar(request):
    return render(request, 'tienda/admin/Agregar.html')
def Listado(request):
    return render(request, 'tienda/admin/Listado.html')

#Seccion agregar
def AgregarN(request):
    nin = 1
    contexto = {
        "Nintendo": nin
    }
    return render(request, 'tienda/admin/Secciones/AgregarN.html',contexto)
def AgregarNintendo(request):
    nombreN = request.POST['NameGameN']
    descripcionN = request.POST['DescripcionN']
    precioN = request.POST['PrecioN']
    imagenN = request.FILES['FotoVN']
    seccionN = request.POST['SeccionVN']
    
    registroSeccionN = Seccion.objects.get(id_seccions = seccionN)

    Videojuegos.objects.create(nombrev = nombreN, descripcion = descripcionN,
                               precio = precioN, imagenv = imagenN, seccion = registroSeccionN)
    return redirect(AgregarN)


def AgregarP(request):
    Play = 2
    contexto = {
        "Playstation": Play
    }
    return render(request, 'tienda/admin/Secciones/AgregarP.html', contexto)
def AgregarPlaystation(request):
    nombreP = request.POST['NameGameP']
    descripcionP = request.POST['DescripcionP']
    precioP = request.POST['PrecioP']
    imagenP = request.FILES['fotoP']
    seccionP = request.POST['SeccionVP']
    
    registroSeccionP = Seccion.objects.get(id_seccions = seccionP)

    Videojuegos.objects.create(nombrev = nombreP, descripcion = descripcionP,
                               precio = precioP, imagenv = imagenP, seccion = registroSeccionP)
    return redirect(AgregarP)

def AgregarPC(request):
    Compu = 4
    contexto = {
        "PC": Compu
    }
    return render(request, 'tienda/admin/Secciones/AgregarPC.html',contexto)
def AgregarPCJuego(request):
    nombrePC = request.POST['NameGamePc']
    descripcionPC = request.POST['DescripcionPc']
    precioPC = request.POST['PrecioPc']
    imagenPC = request.FILES['FotoPc']
    seccionPC = request.POST['SeccionVPC']
    
    registroSeccionPC = Seccion.objects.get(id_seccions = seccionPC)

    Videojuegos.objects.create(nombrev = nombrePC, descripcion = descripcionPC,
                               precio = precioPC, imagenv = imagenPC, seccion = registroSeccionPC)
    return redirect(AgregarPC)

def AgregarX(request):
    Xbo = 3
    contexto = {
        "Xbox": Xbo
    }
    return render(request, 'tienda/admin/Secciones/AgregarX.html',contexto)
def AgregarXbox(request):
    nombreX = request.POST['NameGameX']
    descripcionX = request.POST['DescripcionX']
    precioX = request.POST['PrecioX']
    imagenX = request.FILES['FotoX']
    seccionX = request.POST['SeccionVX']
    
    registroSeccionX = Seccion.objects.get(id_seccions = seccionX)

    Videojuegos.objects.create(nombrev = nombreX, descripcion = descripcionX,
                               precio = precioX, imagenv = imagenX, seccion = registroSeccionX)
    return redirect(AgregarX)

#Modificar Usuarios
def Listado_Usuarios(request):
    listado = Usuario.objects.all()
    contexto = {
        "listadoUsuarios":listado
    }

    return render(request, 'tienda/admin/Listado_Usuarios.html',contexto)

def EliminarUsuario(request,id):
    user = Usuario.objects.get(id_usuariou = id)
    user.delete()
    return redirect('Listado_Usuarios')

#modificar Productos
def Modificar(request, id):
    Videojuego = Videojuegos.objects.get(id_juego = id)
    listado = Seccion.objects.all()
    contexto = {
        "datos": Videojuego,
        "ListadoS": listado
    }
    return render(request, 'tienda/admin/Modificar.html',contexto)

def ModificarJuego(request):
    v_id = request.POST['IDV']
    nombrev = request.POST['NameGameV']
    descripcionv = request.POST['DescripcionV']
    preciov = request.POST['PrecioV']
    imagenvid = request.FILES['FotoV']
    seccionv = request.POST['SeccionV']

    videojuego = Videojuegos.objects.get(id_juego = v_id)
    seccionvi = Seccion.objects.get(id_seccions = seccionv)
    videojuego.nombrev = nombrev
    videojuego.descripcion = descripcionv
    videojuego.precio = preciov
    videojuego.imagenv = imagenvid
    videojuego.seccion = seccionvi

    videojuego.save()
    return redirect('Listado_Videojuegos')

def Listado_Videojuegos(request):
    listado = Videojuegos.objects.all()
    contexto = {
        "listadoVideojuegos":listado
    }
    return render(request, 'tienda/admin/Listado_Videojuegos.html',contexto)

#Eliminar VideoJuegos
def EliminarVideoJuego(request,id):
    videojuego = Videojuegos.objects.get(id_juego = id)
    videojuego.delete()
    return redirect('Listado_Videojuegos')

