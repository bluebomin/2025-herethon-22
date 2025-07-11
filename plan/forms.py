# forms.py
from django import forms
from .models import Plan, JOB_TYPE_CHOICES, REGION_CHOICES # 필요한 CHOICES를 import 합니다.
import json

class PlanForm(forms.ModelForm):
    strengths = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    desired_job = forms.ChoiceField(choices=JOB_TYPE_CHOICES)
    desired_region = forms.ChoiceField(choices=REGION_CHOICES)

    class Meta:
        model = Plan
        fields = [
            'desired_job',
            'desired_region',
            'career_gap_years', # 이 필드는 views.py에서 계산되므로, 폼에서 직접 받지 않는다면 HiddenInput 등을 고려해야 합니다.
                                # 현재 views.py에서 수동으로 계산하여 Plan 객체에 할당하므로, 폼의 fields에는 있어도 크게 상관 없습니다.
            'strengths',
            'resume',
            'goal'
        ]
        widgets = {
            'start_year': forms.NumberInput(attrs={'class': 'input-year'}), # models.py에 있지만 fields에 없는 경우, 폼에서 처리하려면 추가해야 함
            'end_year': forms.NumberInput(attrs={'class': 'input-year'}),   # models.py에 있지만 fields에 없는 경우, 폼에서 처리하려면 추가해야 함
            'resume': forms.ClearableFileInput(), # 파일 입력 위젯
            'goal': forms.Textarea(attrs={
                'class': 'textarea',
                'id': 'TA',
                'placeholder': '재취업 목표를 작성해 보세요. :)',
            }),
            # 'strengths': forms.Textarea(attrs={'class': 'dropdown'}), # HiddenInput을 사용했으므로 이 부분은 필요 없음
        }