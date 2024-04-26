"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from apps.authentication.views import UserViewSet
from apps.cliente.views import ClienteViewSet, ProveedorViewSet
from apps.inventario.views import (
    ProductoCategoriaViewSet,
    ProductoViewSet,
    InventarioViewSet,
    OrdenCompraViewSet,
    CompraProductoViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productoCategorias', ProductoCategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'ordenCompra', OrdenCompraViewSet)
router.register(r'compraProducto', CompraProductoViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include('rest_framework.urls', namespace='auth')),
                  path('api/', include(router.urls)),
                  path('', include('apps.authentication.urls')),
                  path('', include('apps.inventario.urls')),
                  path('', include('apps.cart.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
