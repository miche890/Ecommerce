from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(
                request,
                'authentication/login.html',
                {
                    'error_message': 'Usuario o contraseña incorrectos.'
                }
            )

    else:
        return render(request, 'authentication/login.html')

@login_required()
def perfil(request):
    return render(request, 'authentication/perfil.html')


@login_required()
def cerrar_sesion(request):
    logout(request)
    return redirect('index')
