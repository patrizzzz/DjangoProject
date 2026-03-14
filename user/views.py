from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Register_user
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save()

# Create your views here.
