# forms.py
from django import forms
from .models import Plan, JOB_TYPE_CHOICES, REGION_CHOICES
import json

class PlanForm(forms.ModelForm):
    strengths = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    desired_job = forms.ChoiceField(choices=JOB_TYPE_CHOICES)
    desired_region = forms.ChoiceField(choices=REGION_CHOICES)
    career_gap_years = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-year'}))

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
