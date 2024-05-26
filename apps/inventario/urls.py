from django.urls import path, include
from .views import (
    index,
    lista_productos,
    info_producto
)

urlpatterns = [
    path('', index, name='index'),
    path('productos', lista_productos, name='productos'),
    path('productos/<int:producto_id>', info_producto, name='producto'),
]
