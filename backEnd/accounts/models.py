import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

lenOfImages = 10

def user_directory_path(instance, filename):
    return f'profile_images/{instance.username}/{filename}'

def generate_hash(nickname, birthday, gender):
    input_str = f"{nickname}-{birthday}-{gender}"
    # SHA-256 해시 생성
    hash_object = hashlib.sha256(input_str.encode())
    # 해시 값을 16진수 문자열로 변환 후, 정수로 변환
    hash_value = int(hash_object.hexdigest(), 16)
    return hash_value

def hash(nickname, birthday, gender):
    hash_value = generate_hash(nickname, birthday, gender)
    return hash_value % lenOfImages + 1

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # 필드를 추가
        nickname = data.get("nickname")
        birthday = data.get("birthday")
        gender = data.get("gender")
        address = data.get("address")
        asset = data.get("asset")
        salary = data.get("salary")
        print(salary)
        interest_industry = data.get("interest_industry")
        profile_img_index = hash(str(nickname), str(birthday), str(gender))

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if birthday:
            user_field(user, "birthday", birthday.strftime('%Y-%m-%d'))
        if gender:
            user_field(user, "gender", gender)
        if address:
            user_field(user, "address", address)
        if profile_img_index:
            user_field(user, "profile_img_index", str(profile_img_index))
        if asset is not None:
            asset = str(asset)
            user_field(user, "asset", asset)
        if salary is not None:
            salary = str(salary)
            user_field(user, "salary", salary)
        if interest_industry:
            user_field(user, "interest_industry", interest_industry)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
            self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user

# Create your models here.
class User(AbstractUser):
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
        ('운송','운송'),
        ('미디어','미디어'),
        ('스포츠','스포츠'),
        ('복지','복지'),
    )
    nickname = models.CharField(max_length=20)
    birthday = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_img_index = models.IntegerField()
    asset = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    interest_industry = models.CharField(max_length=20, choices=JOB_CHOICES, null=True)