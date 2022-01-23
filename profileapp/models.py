from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #일대일 매핑,
    #on_delete -> 매핑된 객체가 사라질 때 같이 사라지게끔(CASCADE) 해줌
    #related_name -> 이렇게 해주면 user객체에서 request.user.profile 처럼 이렇게 바로 연결해줄 수 있게 해줌
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    #setting.py 에 media root를 'media/'로 해뒀으니 이렇게하면 media/profile 밑으로 저장 됨
    image = models.ImageField(upload_to = 'profile/', null=True)

    nickname = models.CharField(max_length=20, unique=True)

    message = models.CharField(max_length=100, null=True)