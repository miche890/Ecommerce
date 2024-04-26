from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.middleware.csrf import get_token

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework import viewsets

from .serializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing User instances.

    This ViewSet handles CRUD operations for User instances. It includes authentication
    classes such as SessionAuthentication, BasicAuthentication, and TokenAuthentication
    to ensure secure access. Only authenticated and admin users are allowed to perform
    operations on User instances.

    Attributes:
        authentication_classes (list): List of authentication classes for the view.
        permission_classes (list): List of permission classes for the view.
        queryset (QuerySet): QuerySet containing all User instances.
        serializer_class (Serializer): Serializer class used for User instances.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CSRFTokenView(APIView):
    """
    A view to retrieve the CSRF token.

    This view allows any user to retrieve the CSRF token for use in forms
    that require CSRF protection. It returns the CSRF token as a JSON
    response with the key 'csrf_token'.

    Methods:
        - get: Retrieves the CSRF token and returns it as a JSON response.

    Permissions:
        - AllowAny: Allows any user to access this view.

    Usage:
        Make a GET request to this view to obtain the CSRF token.

    Example Response:
        {
            "csrf_token": "generated_csrf_token_value"
        }
    """
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        """
        Retrieve the CSRF token.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            Response: A JSON response containing the CSRF token.
        """
        csrf_token = get_token(request)
        return Response(data={'csrf_token': csrf_token}, status=200)


class CustomAuthToken(ObtainAuthToken):
    """
    A custom authentication view for obtaining authentication tokens.

    This view extends Django REST Framework's ObtainAuthToken view to provide
    additional functionality when authenticating users and generating tokens.

    Methods:
        - post: Validates user credentials and generates an authentication token.

    Usage:
        Send a POST request to this view with user credentials to obtain an authentication token.

    Request Data:
        - username (str): The username of the user.
        - password (str): The password of the user.
    """

    def post(self, request, *args, **kwargs):
        """
        Authenticate user and generate authentication token.

        Parameters:
            request (HttpRequest): The POST request object containing user credentials.

        Returns:
            Response: A JSON response containing the authentication token and user information.
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'token': token.key,
                    'user_id': user.pk,
                    'username': user.username,
                    'status': HTTP_200_OK
                }, status=HTTP_200_OK
            )
        return Response(
            {
                'errors': serializer.errors,
                'status': HTTP_400_BAD_REQUEST
            }, status=HTTP_400_BAD_REQUEST
        )


class CustomLogout(APIView):
    """
    A custom view for logging out users by deleting their authentication token.

    This view requires TokenAuthentication for authentication and IsAuthenticated
    permission to allow only authenticated users to log out.

    Methods:
        - post: Logs out the authenticated user by deleting their authentication token.

    Usage:
        Send a POST request to this view to log out the authenticated user.

    Example Response (Success):
        {
            "message": "Logout successful",
            "status": 200
        }
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        """
        Log out the authenticated user by deleting their authentication token.

        Parameters:
            request (HttpRequest): The POST request object.

        Returns:
            Response: A JSON response indicating successful logout.
        """
        request.user.auth_token.delete()
        return Response(
            {
                'message': 'Logout successful', 'status': HTTP_200_OK
            },
            status=HTTP_200_OK
        )


class CurrenUser(APIView):
    """
    A view to retrieve information about the current authenticated user.

    This view requires authentication and permission to retrieve information
    about the currently authenticated user.

    Methods:
        - get: Retrieves information about the current authenticated user.

    Usage:
        Make a GET request to this view to obtain information about the current user.

    Example Response:
        {
            "id": "user_id",
            "username": "username",
            "email": "user_email@example.com",
            "fullname": "User Full Name",
            "status": 200
        }
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        """
        Retrieve information about the current authenticated user.

        Parameters:
            request (HttpRequest): The GET request object.

        Returns:
            Response: A JSON response containing information about the current user.
        """
        user = request.user
        return Response(
            {
                'id': user.pk,
                'username': user.username,
                'email': user.email,
                'fullname': user.get_full_name(),
            },
            status=HTTP_200_OK
        )


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Usuario o contraseña incorrectos.'})

    else:
        return render(request, 'authentication/login.html')

@login_required()
def perfil(request):
    return render(request, 'authentication/perfil.html')



