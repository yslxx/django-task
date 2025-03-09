from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser를 상속받아 커스텀 사용자 모델 생성 

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length = 100, unique = True) # 사용자마다 별명을 가질 수 있도록 설정. 
    