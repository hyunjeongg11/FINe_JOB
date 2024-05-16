from .models import Age_Board, Age_Comment, Free_Board, Free_Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class Age_BoardListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)

    class Meta:
        model = Age_Board
        fields = ('id', 'title', 'content', 'nickname', 'created_at')


class Age_CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Age_Comment
        fields = '__all__'
        read_only_fields = ('board', 'user')


class Age_BoardSerializer(serializers.ModelSerializer):
    age_comment = Age_CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='age_comment.count', read_only=True)
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)
    user = UsernameSerializer(read_only=True)
    
    class Meta:
        model = Age_Board
        fields = '__all__'
        read_only_fields = ('user',)


# class DetailUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailUser
#         fields = ('address', )

class Free_BoardListSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.detailuser.address', read_only=True)

    class Meta:
        model = Free_Board
        fields = ('id', 'title', 'content', 'address', 'created_at')


class Free_CommentSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.detailuser.address', read_only=True)
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Free_Comment
        fields = '__all__'
        read_only_fields = ('board', 'user')


class Free_BoardSerializer(serializers.ModelSerializer):
    free_comment = Free_CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='free_comment.count', read_only=True)
    address = serializers.CharField(source='user.detailuser.address', read_only=True)
    user = UsernameSerializer(read_only=True)
    
    class Meta:
        model = Free_Board
        fields = '__all__'
        read_only_fields = ('user',)