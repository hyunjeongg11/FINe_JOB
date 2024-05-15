# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Age_Board, Age_Comment, Free_Board, Free_Comment
from .serializers import Age_BoardListSerializer, Age_BoardSerializer, Age_CommentSerializer, Free_BoardListSerializer, Free_BoardSerializer, Free_CommentSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


User = get_user_model()


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def age_list(request):
    if request.method == 'GET':
        boards = get_list_or_404(Age_Board)
        serializer = Age_BoardListSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Age_BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def age_detail(request, age_pk):
    board = get_object_or_404(Age_Board, pk=age_pk)

    if request.method == 'GET':
        serializer = Age_BoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = Age_BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def age_comment_create(request, age_pk):
    board = get_object_or_404(Age_Board, pk=age_pk)
    serializer = Age_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def age_comment_detail(request, comment_pk):
    comment = Age_Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def free_list(request):
    if request.method == 'GET':
        boards = get_list_or_404(Free_Board)
        serializer = Free_BoardListSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Free_BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def free_detail(request, free_pk):
    board = get_object_or_404(Free_Board, pk=free_pk)

    if request.method == 'GET':
        serializer = Free_BoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = Free_BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def free_comment_create(request, free_pk):
    board = get_object_or_404(Free_Board, pk=free_pk)
    serializer = Free_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def free_comment_detail(request, comment_pk):
    comment = Free_Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_logs(request):
    age_boards = Age_Board.objects.filter(user=request.user)
    age_comments = Age_Comment.objects.filter(user=request.user)
    free_boards = Free_Board.objects.filter(user=request.user)
    free_comments = Free_Comment.objects.filter(user=request.user)

    response_data = {
        'age_boards': Age_BoardListSerializer(age_boards, many=True).data,
        'age_comments': Age_CommentSerializer(age_comments, many=True).data,
        'free_boards': Free_BoardListSerializer(free_boards, many=True).data,
        'free_comments': Free_CommentSerializer(free_comments, many=True).data,
    }

    return JsonResponse(response_data, status=200)