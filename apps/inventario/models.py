from django.contrib.auth.models import User
from django.db import models

import cloudinary
from cloudinary.models import CloudinaryField

from apps.cliente.models import Proveedor


# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(max_length=500, default='', verbose_name='Descripcion')
    destacada = models.BooleanField(default=False, verbose_name='Destacada')

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    price = models.FloatField(max_length=50, verbose_name='Precio')
    imagen = CloudinaryField(resource_type='image', verbose_name='Imagen', default='')
    description = models.TextField(max_length=250, verbose_name='Descripcion')
    proveedor = models.ForeignKey(Proveedor, default=1, on_delete=models.CASCADE, verbose_name='Proveedor')

    class Meta:
        db_table = 'producto'
        verbose_name_plural = 'Productos'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Inventario(models.Model):
    product = models.OneToOneField(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'inventario'
        verbose_name_plural = 'Inventario'
        ordering = ['-id']

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)


class OrdenCompra(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
        ('pagado', 'Pagado')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendiente', verbose_name='Estado')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    date = models.DateTimeField(auto_now=True, verbose_name='Fecha de orden')
    products = models.ManyToManyField(Producto, through='CompraProducto', verbose_name='Productos')

    class Meta:
        db_table = 'orden_compra'
        verbose_name_plural = 'Ordenes de compra'
        ordering = ['-id']

    def __str__(self):
        return str(self.id)


class CompraProducto(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, verbose_name='Orden de compra')
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(default=1, verbose_name='Cantidad')

    class Meta:
        db_table = 'compra_producto'
        verbose_name_plural = 'Compras de producto'
        ordering = ['-id']

    def __str__(self):
        return (
                str(self.id) +
                '- Orden de compra:' + str(self.orden_compra) +
                '- Producto:' + str(self.product.name) +
                ' - Cantidad:' + str(self.quantity)
        )
