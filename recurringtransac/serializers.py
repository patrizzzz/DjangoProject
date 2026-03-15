from rest_framework import serializers
from .models import RecurringtransacConfig

class RecurringConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringtransacConfig
        fields = '__all__'