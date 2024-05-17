from django.db import models
from django.conf import settings

class JobInfo(models.Model):
    keyword = models.TextField() # 분류
    title = models.TextField() # 제목
    company = models.TextField() # 회사
    url = models.TextField() # sarami url
    deadline = models.TextField() # 마감기한
    location = models.TextField() # 근무지
    experience = models.TextField() # 경력사항
    requirement = models.TextField() # 요구조건
    jobtype = models.TextField() # 근로방식
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, related_name='like_job_info') # 관심 공고