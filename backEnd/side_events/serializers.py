from .models import TodayLuck
from rest_framework import serializers


class TodayLuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayLuck
        fields = '__all__'