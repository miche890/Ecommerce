from django.shortcuts import render, redirect

from apps.cart.cart import Cart
from apps.inventario.models import Producto
from apps.cart.context_processor import total_cart


# Create your views here.

def agregar_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.add(producto)
    return redirect('index')


def eliminar_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.remove(producto)
    return redirect('index')


def restar_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.decrement(producto)
    return redirect('index')


def limpiar_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('index')


def ver_cart(request):
    cart = Cart(request).cart.items()
    total = total_cart(request)
    productos_cart = []
    for key, value in cart:
        productos_cart.append(value)
    print(productos_cart)
    print(total)
    return render(request, 'shop/shopping_cart.html', {'productos_cart': productos_cart, 'total': total})
