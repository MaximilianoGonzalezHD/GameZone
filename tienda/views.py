from django.shortcuts import render

# Create your views here.
#Paginas Principales
def tienda(request):
    return render(request,'tienda/inicio/tienda.html')

#Secciones
def seccion_playstation(request):
    return render(request,'tienda/productos/Seccion_Play/seccion_playstation.html')