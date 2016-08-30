
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth

from rest_framework import generics, response, status, permissions

from .permissions import IsNotAuthenticated
from .serializers import (
    RegisterSerializer, LoginSerializer, LogOutSerializer)


class Register(generics.CreateAPIView):
    """
    api to register user
    """
    serializer_class = RegisterSerializer
    permission_classes = (IsNotAuthenticated, )

    def create(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'message': _('Logged in successfully'),
            }
            return response.Response(response_data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()
        auth.login(self.request, serializer.instance)


class Login(generics.GenericAPIView):

    """
    Signin using your email address and password
    """
    serializer_class = LoginSerializer
    permission_classes = (IsNotAuthenticated, )

    def post(self, request, format=None):
        """
        Authenticate User againest credentials & return Authorization token
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            auth.login(request, serializer.instance)
            response_data = {
                'message': _('Logged in successfully'),
            }
            return response.Response(response_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOut(generics.GenericAPIView):
    """
    api to unauthenticate/logout the user
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LogOutSerializer

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        response_data = {
            'message': _('Logged out successfully'),
        }
        return response.Response(response_data, status=status.HTTP_200_OK)
