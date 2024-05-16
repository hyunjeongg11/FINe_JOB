from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    search_date = models.DateField()
    cur_unit = models.CharField(max_length=100) # 통화코드
    cur_nm = models.TextField() # 국가/통화명
    ttb = models.TextField() # 전신환(송금) 받을때
    tts = models.TextField() # 전신환 (송금) 보낼때
    deal_bas_r = models.TextField() # 매매 기준율