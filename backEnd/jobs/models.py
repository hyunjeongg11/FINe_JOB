from django.db import models

# Create your models here.
class JobInfo(models.Model):
    title = models.TextField() # 제목
    company = models.TextField() # 회사
    url = models.TextField() # sarami url
    deadline = models.TextField() # 마감기한
    location = models.TextField() # 근무지
    experience = models.TextField() # 경력사항
    requirement = models.TextField() # 요구조건
    jobtype = models.TextField() # 근로방식