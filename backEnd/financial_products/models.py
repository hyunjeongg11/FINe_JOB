from django.db import models
from django.conf import settings

# Create your models here.
class Deposit_Products(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    dcls_month = models.TextField() # 공시 제출월
    kor_co_nm = models.TextField() # 금융회사명
    fin_prdt_nm = models.TextField() # 금융상품명
    join_way = models.TextField() # 가입방법
    join_member = models.TextField() # 가입대상
    spcl_cnd = models.TextField() # 우대조건
    etc_note = models.TextField() # 금융상품설명
    join_deny = models.IntegerField() #  가입제한 (1: 제한X, 2:서민전용, 3: 일부제한)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null= True, related_name= 'like_deposit') # 찜한 유저
    

class Deposit_Options(models.Model):
    deposit_product = models.ForeignKey(Deposit_Products, on_delete=models.CASCADE, related_name='deposit_options')
    fin_prdt_cd = models.TextField() # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    intr_rate = models.FloatField(null= True, default=-1) # 저축금리
    intr_rate2 = models.FloatField(null= True, default=-1) # 최고 우대 금리
    save_trm = models.IntegerField() # 저축기간 (단위:개월)


class Saving_Products(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    dcls_month = models.TextField() # 공시 제출월
    kor_co_nm = models.TextField() # 금융회사명
    fin_prdt_nm = models.TextField() # 금융상품명
    join_way = models.TextField() # 가입방법
    join_member = models.TextField() # 가입대상
    spcl_cnd = models.TextField() # 우대조건
    etc_note = models.TextField() # 금융상품설명
    join_deny = models.IntegerField() #  가입제한 (1: 제한X, 2:서민전용, 3: 일부제한)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null= True, related_name= 'like_saving') # 찜한 유저


class Saving_Options(models.Model):
    saving_product = models.ForeignKey(Saving_Products, on_delete=models.CASCADE, related_name='saving_options')
    fin_prdt_cd = models.TextField() # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    intr_rate = models.FloatField(null= True, default=-1) # 저축금리
    intr_rate2 = models.FloatField(null= True, default=-1) # 최고 우대 금리
    save_trm = models.IntegerField() # 저축기간 (단위:개월)
    rsrv_type = models.TextField() # 적립 유형