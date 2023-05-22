from django.db import models

# Create your models here.
class Rol (models.Model):
    id_rolr = models.AutoField(primary_key=True)
    nombrer = models.CharField(max_length=30)

class Usuario (models.Model):
    id_usuariou = models.AutoField(primary_key=True)
    emailu = models.CharField(max_length=20)
    nombre_usuariou = models.CharField(max_length=15)
    contrasenau = models.CharField(max_length=15)
    nombreu = models.CharField(blank,max_length=30)
    imagenu
    rol = models.Foreignkey(Rol,on_delete=models.CASCADE)

class Compra (models.Model):
    id_comprac = models.AutoField(primary_key=True)
    fechac = models.DataField(verbose_name='Fecha de compra')
    rutc = models.CharField(max_length=16)
    totalc = models.integerField(verbose_name='Total De la Compra')
    id_usuario = models.Foreignkey(Usuario,on_delete=models.CASCADE)
    id_detalles = models.Foreignkey(Detalles_compra)

class Detalles_compra (models.Model):
    id_detallesc = models.AutoField(primary_key=True)
    subtotal = models.integerField (verbose_name='Subtotal de la compra')
    cantidad = models.integerField(verbose_name='cantidad de productos')
    id_juego = models.Foreignkey(Videojuegos,on_delete=models.CASCADE)

class Videojuegos (models.Model):
    id_juego = models.AutoField(primary_key=True)
    nombrev = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.integerField(verbose_name='Precio de videojuegos')
    imagenv
    seccion = models.Foreignkey(Seccion,on_delete=models.CASCADE)


class Seccion (models.Model):
        id_seccions = models.AutoField(primary_key=True)
        nombres = models.CharField(max_length=30)