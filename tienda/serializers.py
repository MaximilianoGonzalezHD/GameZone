from tienda.models import Usuario, Compra, Detallesc, Carrito, ItemCarrito, Videojuegos
from django.contrib.auth.models import User
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class DetallescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallesc
        fields = '__all__'


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'


class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class VideojuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuegos
        fields = '__all__'