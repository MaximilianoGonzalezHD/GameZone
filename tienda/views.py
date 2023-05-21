from django.shortcuts import render

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

#productos
def bloodborne(request):
    return render(request,'tienda/productos/Seccion_Play/bloodborne.html')
#Paginas iniciales
def registro(request):
    return render(request, 'tienda/inicio/registro.html')

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

#Seccion agregar
def Agregar(request):
    return render(request, 'tienda/admin/Agregar.html')

def AgregarN(request):
    return render(request, 'tienda/admin/Secciones/AgregarN.html')

def AgregarP(request):
    return render(request, 'tienda/admin/Secciones/AgregarP.html')

def AgregarPC(request):
    return render(request, 'tienda/admin/Secciones/AgregarPC.html')

def AgregarX(request):
    return render(request, 'tienda/admin/Secciones/AgregarX.html')


#Eliminar Productos
def Eliminar(request):
    return render(request, 'tienda/admin/Eliminar.html')
#modificar Productos
def Modificar(request):
    return render(request, 'tienda/admin/Modificar.html')