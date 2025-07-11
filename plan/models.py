from django.db import models
from django.contrib.auth.models import User

JOB_TYPE_CHOICES = [
    ('planning', '기획/전략'),
    ('development', 'IT/개발/데이터'),
    ('manufacturing', '생산/제조'),
    ('contents', '콘텐츠/미디어'),
    ('marketing', '마케팅/홍보/MD'),
    ('customer_service', '고객상담/CS'),
    ('construction', '건축/시설관리'),
    ('finance', '금융/보험'),
    ('accounting', '회계/세무/재무'),
    ('logistics', '물류/운송'),
    ('healthcare', '의료/간호'),
    ('public', '공공/복지'),
    ('design', '디자인'),
    ('operation', '운영/서비스업'),
    ('education', '교육/강의'),
    ('hr', '인사/사무/총무'),
]

REGION_CHOICES = [
    ('seoul', '서울'),
    ('gyeonggi', '경기/인천'),
    ('busan', '부산/울산/경남'),
    ('daegu', '대구/경북'),
    ('gwangju', '광주/전남/전북'),
    ('daejeon', '대전/충남/충북'),
    ('gangwon', '강원'),
    ('jeju', '제주'),
]

class Plan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desired_job = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES)
    desired_region = models.CharField(max_length=100, choices=REGION_CHOICES)
    career_gap_years = models.PositiveIntegerField()
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    strengths = models.JSONField(default=list, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    goal = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}의 재도전 계획"


# forms.py
from django import forms
from .models import Plan, JOB_TYPE_CHOICES, REGION_CHOICES

class PlanForm(forms.ModelForm):
    strengths = forms.CharField(widget=forms.HiddenInput(), required=False)
    desired_job = forms.ChoiceField(choices=JOB_TYPE_CHOICES)
    desired_region = forms.ChoiceField(choices=REGION_CHOICES)

    class Meta:
        model = Plan
        fields = [
            'desired_job',
            'desired_region',
            'career_gap_years',
            'strengths',
            'resume',
            'goal'
        ]
        widgets = {
            'resume': forms.ClearableFileInput(attrs={
                'id': 'resumeInput',
                'class': 'file-input',
            }),
            'goal': forms.Textarea(attrs={
                'class': 'textarea',
                'id': 'TA',
                'placeholder': '재취업 목표를 작성해 보세요. :)',
            }),
        }