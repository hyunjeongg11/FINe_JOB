from .models import TodayLuck, FAQ
from rest_framework import serializers


class TodayLuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayLuck
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'