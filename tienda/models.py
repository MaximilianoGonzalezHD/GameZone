from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Rol (models.Model):
    id_rolr = models.AutoField(primary_key=True)
    nombrer = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nombrer
def get_default_image2():
    return 'tienda/static/tienda/IMG/predeterminado.png'
class Usuario (models.Model):
    id_usuariou = models.IntegerField(primary_key=True)
    emailu = models.CharField(max_length=30)
    nombre_usuariou = models.CharField(max_length=20)
    contrasenau = models.CharField(max_length=50)
    nombreu = models.CharField(blank=True,max_length=30)
    imagenu = models.ImageField(verbose_name="Imagen De Usuario",upload_to="ImagenUser", default=get_default_image2)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre_usuariou

class Seccion (models.Model):
    id_seccions = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nombres   
    
def get_default_image():
    return 'media/IMG/GameZone.jpg'

class Videojuegos (models.Model):
    id_juego = models.AutoField(primary_key=True)
    nombrev = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=800)
    precio = models.FloatField(verbose_name='Precio de videojuegos')
    imagenv = models.ImageField(blank=True,verbose_name="Imagen de videojuegos", upload_to="ImagenVideojuegos",null=True, default=get_default_image)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=slugify(nombrev))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombrev)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
            return self.nombrev


class Compra(models.Model):
    id_comprac = models.AutoField(primary_key=True)
    fechac = models.DateField(verbose_name='Fecha de compra', default=timezone.now)
    rutc = models.CharField(max_length=16, default=None)
    totalc = models.IntegerField(verbose_name='Total de la compra',default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f'Compra {self.id_comprac}'

class Detallesc(models.Model):
    id_detallesc = models.AutoField(primary_key=True)
    subtotal = models.FloatField(verbose_name='Subtotal de la compra',default=None)
    cantidad = models.IntegerField(verbose_name='Cantidad de productos',default=None)
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE,default=None)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f'Detallesc {self.id_detallesc} - Compra {self.compra.id_comprac}'
    
class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Carrito {self.id_carrito} - Usuario {self.usuario.nombre_usuariou}'

class ItemCarrito(models.Model):
    id_itemcarrito = models.AutoField(primary_key=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Item {self.id_itemcarrito} - Carrito {self.carrito.id_carrito}'