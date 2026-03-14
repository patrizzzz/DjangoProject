from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return category.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# Create your views here.
