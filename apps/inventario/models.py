from django.db import models

# Create your models here.


class ProductoCategoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(max_length=500, default='', verbose_name='Descripcion')

    class Meta:
        db_table = 'producto_categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    category = models.ForeignKey(ProductoCategoria, on_delete=models.CASCADE, verbose_name='Categoria')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    image = models.ImageField(upload_to='products', verbose_name='Imagen')
    description = models.TextField(max_length=250, verbose_name='Descripcion')

    class Meta:
        db_table = 'producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name


class Inventario(models.Model):
    product = models.ForeignKey(Producto, unique=True, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'inventario'
        verbose_name_plural = 'Inventario'

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)
