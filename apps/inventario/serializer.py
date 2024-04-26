from rest_framework import serializers
from .models import Categoria, Producto, Inventario, OrdenCompra, CompraProducto


class ProductoCategoriaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = '__all__'

    @staticmethod
    def get_id(obj):
        return obj.id


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    @staticmethod
    def get_id(obj):
        return obj.id


class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Inventario
        fields = '__all__'

    @staticmethod
    def get_id(obj):
        return obj.id


class OrdenCompraSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = OrdenCompra
        fields = '__all__'

    @staticmethod
    def get_id(obj):
        return obj.id


class CompraProductoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = CompraProducto
        fields = '__all__'

    @staticmethod
    def get_id(obj):
        return obj.id
