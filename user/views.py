from django.shortcuts import render

from .serializers import RegisterSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token = Token.objects.create(user_id = response.data['id'])
        response.data['token'] = token.key
        return response