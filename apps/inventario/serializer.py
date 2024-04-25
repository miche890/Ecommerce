from rest_framework import serializers
from .models import ProductoCategoria, Producto, Inventario


class ProductoCategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductoCategoria
        fields = '__all__'


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'
