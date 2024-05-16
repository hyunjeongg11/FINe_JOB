from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import JsonResponse 
from .serializers import CustomUserEditSerializer, UserDetailSerializer
from .models import User

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({'msg': 'delete complete'}, status=status.HTTP_200_OK)

# edit user info
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_info(request):
    user = request.user
    serializer = CustomUserEditSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_detail(request, search_name):
    try:
        user = User.objects.get(username=search_name)
        serializer = UserDetailSerializer(user,context={'request': request})
        # user_articles=ArticleSerializer(Article.objects.filter(user=user),many=True)
        # user_comments=CommentSerializer(Comment.objects.filter(user=user),many=True)
        # user_products=user.joined_deposit_products.all()
        # return_product_and_option=[]
        # for item in user_products:
        #     options=item.option.all()
        #     return_product_and_option.append({'product':DepositProductSerializer(item).data,'option':DepositOptionSerializer(options,many=True).data})
        
        # user_products=user.joined_saving_products.all()
        # for item in user_products:
        #     options=item.option.all()
        #     return_product_and_option.append({'product':SavingProductSerializer(item).data,'option':SavingOptionSerializer(options,many=True).data})
        # result={'message':'success','user_articles': user_articles.data, 'user_comments': user_comments.data,'user_data':serializer.data,'user_products':return_product_and_option}
        result={'message':'success','user_data':serializer.data}
        return Response(result, status=status.HTTP_200_OK)
    except:
        return Response({'message':'error'}, status=status.HTTP_404_NOT_FOUND)