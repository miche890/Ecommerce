from django.shortcuts import render, redirect

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductoCategoria, Producto, Inventario, OrdenCompra, CompraProducto
from .serializer import (
    ProductoCategoriaSerializer,
    ProductoSerializer,
    InventarioSerializer,
    OrdenCompraSerializer,
    CompraProductoSerializer
)
from ..cart.cart import Cart


# Create your views here.


class ProductoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = ProductoCategoria.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductoCategoriaSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductoSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    ordering_fields = ['id', 'name', 'price', 'category']


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = InventarioSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['last_updated']
    search_fields = ['product__name']
    ordering_fields = ['id', 'product', 'quantity', 'last_updated']


class OrdenCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenCompra.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = OrdenCompraSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'products']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    ordering_fields = ['id', 'user', 'status', 'date', 'products']


class CompraProductoViewSet(viewsets.ModelViewSet):
    queryset = CompraProducto.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CompraProductoSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product']
    search_fields = ['orden_compra']
    ordering_fields = ['id', 'product', 'orden_compra']


def index(request):
    productos = Producto.objects.all()
    productos_cart = Cart(request).cart.items()
    return render(request, 'index.html', {'productos': productos, 'productos_cart': productos_cart})


