from django.contrib import admin

# Register your models here.
from .models import Cliente, Proveedor


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nit', 'name', 'email', 'active']
    search_fields = ['id', 'nit', 'name', 'email']
    list_filter = ['active']


admin.site.register(Cliente, ClienteAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nit', 'name', 'email', 'active']
    search_fields = ['id', 'nit', 'name', 'email']
    list_filter = ['active']


admin.site.register(Proveedor, ProveedorAdmin)
