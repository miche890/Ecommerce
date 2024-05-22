from django.urls import path, include
from .views import (
    promociones
)

urlpatterns = [
    path('promociones', promociones, name='promociones'),
]
