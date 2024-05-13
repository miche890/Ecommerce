from django.urls import path, include
from .views import (
    index,
    lista_productos
)

urlpatterns = [
    path('', index, name='index'),
    path('productos/', lista_productos, name='productos'),
]
