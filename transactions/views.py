from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transactions
from .serializers import TransactionsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    def get_queryset(self):
        return Transactions.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
