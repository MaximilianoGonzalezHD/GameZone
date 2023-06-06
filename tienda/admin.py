from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Compra,Detallesc,Videojuegos,Seccion,Usuario,Rol
# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Seccion)
admin.site.register(Videojuegos)
admin.site.register(Detallesc)
admin.site.register(Compra)

