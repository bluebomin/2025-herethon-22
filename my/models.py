from django.db import models

# Create your models here.
class MyProfile(models.Model):
    user_name = models.CharField(max_length=10)
    REGION_CHOICES =[        
        ('seoul', '서울'),
        ('gyeonggi', '경기/인천'),
        ('busan', '부산/울산/경남'),
        ('daegu', '대구/경북'),
        ('gwangju', '광주/전남/전북'),
        ('daejeon', '대전/충남/충북'),
        ('gangwon', '강원'),
        ('jeju', '제주'),
    ]
    desired_region = models.CharField(max_length=20, choices=REGION_CHOICES)

    #보유역량 갯수 개발하기

    career_break = models.IntegerField(max_length=5, null=True, blank=True)



