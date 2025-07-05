from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)     # 로그인 기능 만들어지면 나중에 User 모델 참조하게 만들겠습니다

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title