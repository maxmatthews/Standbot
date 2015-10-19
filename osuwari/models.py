from django.db import models

class Meeting(models.Model):
    currentMember = models.CharField(max_length=50)
    channel = models.CharField(max_length=50, default='C0CMUCBBM', primary_key=True)
    meetingOrder = models.CharField(max_length=500)
    questionNum = models.IntegerField(default=1)

