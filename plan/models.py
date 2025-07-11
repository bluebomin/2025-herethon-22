from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desired_job = models.CharField(max_length=100)
    desired_region = models.CharField(max_length=100)
    career_gap_years = models.PositiveIntegerField()
    strengths = models.JSONField(default=list, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    goal = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}의 재도전 계획"

# class Plan(models.Model):
#     desired_job = models.CharField(max_length=255, blank=True)
