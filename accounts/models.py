from django.db import models

# views.py에서 User 모델을 직접 사용하고 있지만 테스트해보려고 조금 수정했습니다

class Temp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp {self.id}"
