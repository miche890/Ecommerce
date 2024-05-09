from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Categoria, Producto, Inventario, OrdenCompra, CompraProducto

from ..cart.cart import Cart


# Create your views here.

def index(request):
    categorias = Categoria.objects.all()

    consulta = request.GET.get('consulta', '')
    if consulta:
        productos = busqueda(consulta)
    else:
        productos = Producto.objects.all()

    # Filtrar productos por categoria
    categoria = request.GET.get('categoria', '')
    if categoria:
        productos = filtro(productos, categoria)

    # Paginar productos
    paginator = Paginator(productos, 2)  # Muestra 20 por pagina
    numero_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_pagina)

    return render(
        request,
        'index.html',
        {
            'categorias': categorias,
            'productos': productos,
            'page_obj': page_obj
        }
    )


def busqueda(consulta):
    productos = Producto.objects.filter(name__icontains=consulta)
    return productos


def filtro(productos, categoria):
    productos = productos.filter(category__name__contains=categoria)
    return productos
