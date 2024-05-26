from django.urls import path, include
from .views import (
    agregar_producto,
    agregar_producto_cantidad,
    restar_producto,
    eliminar_producto,
    limpiar_cart,
    ver_cart
)

urlpatterns = [
    path('agregar_producto/<int:producto_id>', agregar_producto, name='agregar_producto'),
    path('agregar_producto_cantidad/<int:producto_id>', agregar_producto_cantidad, name='agregar_producto_cantidad'),
    path('restar_producto/<int:producto_id>', restar_producto, name='restar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('limpiar_cart', limpiar_cart, name='limpiar_cart'),
    path('ver_cart', ver_cart, name='ver_cart'),
]
