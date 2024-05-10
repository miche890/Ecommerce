from django.contrib import admin
from .models import Categoria, Producto, Inventario, OrdenCompra, CompraProducto

from apps.inventario.models import CompraProducto


# Register your models here.

class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'destacada']
    search_fields = ['id', 'name']


admin.site.register(Categoria, ProductoCategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'price', 'proveedor']
    list_filter = ['category', 'proveedor']
    search_fields = ['id', 'name']


admin.site.register(Producto, ProductoAdmin)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['id', 'product', 'quantity']


admin.site.register(Inventario, InventarioAdmin)


class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'get_products', 'status']
    list_filter = ['date', 'status', 'user']
    search_fields = ['id', 'user__username', 'products__name']

    def get_products(self, obj):
        return ', '.join([p.name for p in obj.products.all()])

    get_products.short_description = 'Productos'


# admin.site.register(OrdenCompra, OrdenCompraAdmin)


class CompraProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'get_product_price', 'quantity', 'orden_compra']
    list_filter = ['orden_compra', 'product']
    search_fields = ['id', 'product__name', 'orden_compra']

    def get_product_price(self, obj):
        return obj.product.price

    get_product_price.short_description = 'Precio'


# admin.site.register(CompraProducto, CompraProductoAdmin)
