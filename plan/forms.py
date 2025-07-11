from django import forms
from .models import Plan
import json

class PlanForm(forms.ModelForm):
    strengths = forms.CharField(widget=forms.HiddenInput(), required=False)  # HiddenInput으로 변경

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


from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        widgets = {
            'desired_job': forms.Select(attrs={'class': 'dropdown'}),
            'desired_region': forms.Select(attrs={'class': 'dropdown'}),
            'start_year': forms.NumberInput(attrs={'class': 'input-year'}),
            'end_year': forms.NumberInput(attrs={'class': 'input-year'}),
            'strengths': forms.Textarea(attrs={'class': 'dropdown'}),
            'goal': forms.Textarea(attrs={'class': 'textarea'}),
        }
