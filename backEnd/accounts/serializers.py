from rest_framework import serializers
from .models import User, DetailUser
from rest_framework import serializers
from django.contrib.auth import get_user_model    


# 유저 프로필 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    
    class Meta:
        model = DetailUser
        fields = '__all__'

