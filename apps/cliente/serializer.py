from rest_framework import serializers
from .models import Cliente, Proveedor


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'