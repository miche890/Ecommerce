from django.shortcuts import render, redirect

from .models import Categoria, Producto, Inventario, OrdenCompra, CompraProducto

from ..cart.cart import Cart


# Create your views here.

def index(request):
    productos = Producto.objects.all()
    productos_cart = Cart(request).cart.items()
    return render(request, 'index.html', {
        'productos': productos,
        'productos_cart': productos_cart
    })
