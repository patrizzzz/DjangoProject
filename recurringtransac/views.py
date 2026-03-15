from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import RecurringtransacConfig
from .serializers import RecurringConfigSerializer

class RecurringConfigViewSet(viewsets.ModelViewSet):
    queryset = RecurringtransacConfig.objects.all()
    serializer_class = RecurringConfigSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return RecurringConfigSerializer

    def get_queryset(self):
        return RecurringtransacConfig.objects.all()


# Create your views here.
