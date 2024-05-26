from django.shortcuts import render, redirect

from apps.cart.cart import Cart
from apps.inventario.models import Producto
from apps.cart.context_processor import total_cart


# Create your views here.

def agregar_producto(request, producto_id):
    if request.user.is_authenticated:
        cart = Cart(request)
        producto = Producto.objects.get(id=producto_id)
        cart.add(producto)
        return redirect('productos')
    else:
        return render(
            request,
            'authentication/login.html',
            {
                'error_message': 'Para poder añadir productos al carrito inicia sesion'
            }
        )


def agregar_producto_cantidad(request, producto_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cantidad = int(request.POST['cantidad'])
            cart = Cart(request)
            producto = Producto.objects.get(id=producto_id)
            cart.add_quantity(producto, cantidad)
            return redirect('productos')
    else:
        return render(
            request,
            'authentication/login.html',
            {
                'error_message': 'Para poder añadir productos al carrito inicia sesion'
            }
        )


def eliminar_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.remove(producto)
    return redirect('ver_cart')


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
    return render(request, 'shop/shopping_cart.html')
