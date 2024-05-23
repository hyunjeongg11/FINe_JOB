from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model    
from dj_rest_auth.registration.serializers import RegisterSerializer
from financial_products.serializers import DepositProductsSerializer, SavingProductsSerializer

# 유저 프로필 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_img_index')

class UserDetailSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.detailuser.address', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'birthday', 'gender', 'address', 'profile_img_index', 'asset', 'salary', 'interest_industry')

class CustomUserEditSerializer(serializers.ModelSerializer):
    # address = serializers.CharField(source='user.detailuser.address', read_only=True)

    class Meta:
        model = User
        fields = ['nickname', 'birthday', 'address', 'gender', 'profile_img', 'asset', 'salary', 'interest_industry']
        read_only_fields = ['birthday',]

# 관심 상품 리스트
class UserLikeListSerializer(serializers.ModelSerializer):
    deposit_list = serializers.SerializerMethodField()
    saving_list = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('deposit_list', 'saving_list')

    def get_deposit_list(self, obj):
        return DepositProductsSerializer(obj.like_deposit.all(), many=True).data

    def get_saving_list(self, obj):
        return SavingProductsSerializer(obj.like_saving.all(), many=True).data


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

JOB_CHOICES = (
        # ('모델에 설정할 값', '사람이 읽을수 있는 이름')
        ('IT','IT'),
        ('서비스','서비스'),
        ('금융','금융'),
        ('보험','보험'),
        ('인사','인사'),
        ('노무','노무'),
        ('회계','회계'),
        ('세무','세무'),
        ('재무','재무'),
        ('디자인','디자인'),
        ('생산','생산'),
        ('영업','영업'),
        ('상품기획','상품기획'),
        ('교육','교육'),
        ('R&D','R&D'),
        ('의료','의료'),
        ('건축','건축'),
        ('전기','전기'),
        ('기계','기계'),
        ('고객상담','고객상담'),
        ('운송','운송'),
        ('미디어','미디어'),
        ('스포츠','스포츠'),
        ('복지','복지'),
    )

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=20)
    birthday = serializers.DateField(required=True, format="%Y-%m-%d")
    gender = serializers.ChoiceField(required=True, choices=GENDER_CHOICES, allow_null=True)
    address = serializers.CharField(required=False, max_length=255, allow_null=True)
    profile_img = serializers.ImageField(required=False, allow_null=True, use_url=True)
    asset = serializers.IntegerField(required=False, allow_null=True)
    salary = serializers.IntegerField(required=False, allow_null=True)
    interest_industry = serializers.ChoiceField(required=False, choices=JOB_CHOICES, allow_null=True)

    # def validate_nickname(self, value):
    #     if User.objects.filter(nickname=value).exists():
    #         raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
    #     return value

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'birthday': self.validated_data.get('birthday', ''),
            'gender': self.validated_data.get('gender', ''),
            'address': self.validated_data.get('address', ''),
            'profile_img': self.validated_data.get('profile_img', ''),
            'asset': self.validated_data.get('asset', ''),
            'salary': self.validated_data.get('salary', ''),
            'interest_industry': self.validated_data.get('interest_industry', ''),
        }