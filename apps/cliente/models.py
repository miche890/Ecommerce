from django.db import models


# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=120, verbose_name='Nombre')
    email = models.CharField(max_length=120, blank=True, null=True, verbose_name='Correo electronico')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Direccion')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Telefono')
    contact_name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Nombre del contacto')
    active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        db_table = 'cliente'
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=120, verbose_name='Nombre')
    email = models.CharField(max_length=120, blank=True, null=True, verbose_name='Correo electronico')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Direccion')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Telefono')
    contact_name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Nombre del contacto')
    active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        db_table = 'proveedor'
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.name
