from rest_framework import serializers
from .models import JobInfo

class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfo
        fields = '__all__'
