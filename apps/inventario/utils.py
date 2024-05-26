from apps.inventario.models import Producto


def busqueda(consulta):
    productos = Producto.objects.filter(name__icontains=consulta)
    return productos


def filtro(productos, categoria):
    productos = productos.filter(category__name__contains=categoria)
    return productos


def ordenar(productos, campo):
    productos = productos.order_by(campo)
    return productos


def get_producto(producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        return producto
    except Producto.DoesNotExist:
        message_error = 'Producto no encontrado.'
        return message_error
