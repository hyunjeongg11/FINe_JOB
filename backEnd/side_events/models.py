from django.db import models

class TodayLuck(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class FAQ(models.Model):
    subject = models.TextField()
    url = models.TextField()
    registerDate = models.DateField()