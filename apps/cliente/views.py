from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from .models import Cliente, Proveedor
from .serializer import ClienteSerializer, ProveedorSerializer


# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ClienteSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['active']
    search_fields = ['nit', 'name', 'email', 'active']
    ordering_fields = ['id', 'nit', 'name', 'email']


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProveedorSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['active']
    search_fields = ['nit', 'name', 'email', 'active']
    ordering_fields = ['id', 'nit', 'name', 'email']