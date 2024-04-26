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
from .views import (
    CSRFTokenView,
    CustomAuthToken,
    CustomLogout,
    CurrenUser,
    iniciar_sesion,
    perfil
)

urlpatterns = [
    path('api/auth/login/', CustomAuthToken.as_view(), name='auth-login'),
    path('api/auth/logout/', CustomLogout.as_view(), name='auth-logout'),
    path('api/auth/csrf/', CSRFTokenView.as_view(), name='auth-csrf'),
    path('api/auth/user/', CurrenUser.as_view(), name='auth-user'),
    path('login/', iniciar_sesion, name='login'),
    path('perfil/', perfil, name='perfil'),
]
