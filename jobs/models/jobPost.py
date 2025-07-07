from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    # 추가로 더 구현하겠습니다.
