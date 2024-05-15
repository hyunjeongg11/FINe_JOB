from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return f'profile_images/{instance.user.username}/{filename}'

# Create your models here.
class User(AbstractUser):
    pass


class DetailUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = [
        ("남성", "남성"),
        ("여성", "여성"),
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
        ('운송','운송')
        ('미디어','미디어')
        ('스포츠','스포츠')
        ('복지','복지')
    )
    nickname = models.CharField(max_length=20, null=True)
    birthday = models.CharField(max_length=8, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255, null=True)
    profile_img = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    asset = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    interest_industry = models.CharField(max_length=20, choices=JOB_CHOICES, null=True)