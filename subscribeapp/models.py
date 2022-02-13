import django
from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    #사용자와 그 사용자의 구독정보를 하나로 묶어줘야하기 때문에 (두번 구독할 수 없기 때문 )
    class Meta:
        unique_together = ('user','project')