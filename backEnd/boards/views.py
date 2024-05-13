# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import MMBoard, MMComment, LBoard, LComment
from .serializers import MMBoardListSerializer, MMBoardSerializer, MMCommentSerializer, LBoardListSerializer, LBoardSerializer, LCommentSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


User = get_user_model()


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def moneyMGMT_list(request):
    if request.method == 'GET':
        boards = get_list_or_404(MMBoard)
        serializer = MMBoardListSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MMBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def moneyMGMT_detail(request, moneyMGMT_pk):
    board = get_object_or_404(MMBoard, pk=moneyMGMT_pk)

    if request.method == 'GET':
        serializer = MMBoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = MMBoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def moneyMGMT_comment_create(request, moneyMGMT_pk):
    board = get_object_or_404(MMBoard, pk=moneyMGMT_pk)
    serializer = MMCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def moneyMGMT_comment_detail(request, comment_pk):
    comment = MMComment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def local_list(request):
    if request.method == 'GET':
        boards = get_list_or_404(LBoard)
        serializer = LBoardListSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def local_detail(request, local_pk):
    board = get_object_or_404(LBoard, pk=local_pk)

    if request.method == 'GET':
        serializer = LBoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = LBoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def local_comment_create(request, local_pk):
    board = get_object_or_404(LBoard, pk=local_pk)
    serializer = LCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def local_comment_detail(request, comment_pk):
    comment = LComment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_logs(request):
    mm_boards = MMBoard.objects.filter(user=request.user)
    mm_comments = MMComment.objects.filter(user=request.user)
    l_boards = LBoard.objects.filter(user=request.user)
    l_comments = LComment.objects.filter(user=request.user)

    response_data = {
        'mm_boards': MMBoardListSerializer(mm_boards, many=True).data,
        'mm_comments': MMCommentSerializer(mm_comments, many=True).data,
        'l_boards': LBoardListSerializer(l_boards, many=True).data,
        'l_comments': LCommentSerializer(l_comments, many=True).data,
    }

    return JsonResponse(response_data, status=200)