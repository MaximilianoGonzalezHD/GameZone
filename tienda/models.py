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
    nombreu = models.CharField(blank=True,max_length=30)
    imagenu = models.ImageField(blank=True,verbose_name="Imagen De Usuario",upload_to="ImagenUser")
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)


class Seccion (models.Model):
        id_seccions = models.AutoField(primary_key=True)
        nombres = models.CharField(max_length=30)

class Videojuegos (models.Model):
    id_juego = models.AutoField(primary_key=True)
    nombrev = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField(verbose_name='Precio de videojuegos')
    imagenv = models.ImageField(blank=True,verbose_name="Imagen de videojuegos", upload_to="ImagenVideojuegos")
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)


class Detallesc (models.Model):
    id_detallesc = models.AutoField(primary_key=True)
    subtotal = models.FloatField (verbose_name='Subtotal de la compra')
    cantidad = models.IntegerField(verbose_name='cantidad de productos')
    id_juego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE)

class Compra (models.Model):
    id_comprac = models.AutoField(primary_key=True)
    fechac = models.DateField(verbose_name='Fecha de compra')
    rutc = models.CharField(max_length=16)
    totalc = models.IntegerField(verbose_name='Total De la Compra')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_detalles = models.ForeignKey(Detallesc, on_delete=models.CASCADE)