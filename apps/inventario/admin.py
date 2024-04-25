from django.contrib import admin
from .models import ProductoCategoria, Producto, Inventario


# Register your models here.

class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['id', 'name']


admin.site.register(ProductoCategoria, ProductoCategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'price']
    list_filter = ['category']
    search_fields = ['id', 'name']


admin.site.register(Producto, ProductoAdmin)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['id', 'product', 'quantity']


admin.site.register(Inventario, InventarioAdmin)