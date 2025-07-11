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
