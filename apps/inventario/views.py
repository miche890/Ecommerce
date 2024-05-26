from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Categoria, Producto, Inventario, OrdenCompra, CompraProducto
from .utils import busqueda, filtro, ordenar, get_producto

from ..cart.cart import Cart


# Create your views here.

def index(request):
    return render(request, 'index.html')


def lista_productos(request):
    consulta = request.GET.get('consulta', '')
    if consulta:
        productos = busqueda(consulta)
    else:
        productos = Producto.objects.all()

    # Filtrar productos por categoria
    categoria = request.GET.get('categoria', '')
    if categoria:
        productos = filtro(productos, categoria)

    campo = request.GET.get('campo', '')
    if campo:
        productos = ordenar(productos, campo)

    # Paginar productos
    paginator = Paginator(productos, 20)  # Muestra 20 por pagina
    numero_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_pagina)

    return render(
        request,
        'inventario/index.html',
        {
            'productos': productos,
            'page_obj': page_obj
        }
    )


def info_producto(request, producto_id):
    respuesta = get_producto(producto_id)
    error_message = ""
    producto = None

    if type(respuesta) is str:
        error_message = respuesta
    else:
        producto = respuesta

    return render(
        request,
        'shop/info_producto.html',
        {
            'producto': producto,
            'error_message': error_message,
        }
    )
