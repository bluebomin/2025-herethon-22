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

            'goal': forms.Textarea(attrs={
                'class': 'textarea',
                'id': 'TA',
                'placeholder': '재취업 목표를 작성해 보세요. :)',
            }),
            'resume': forms.ClearableFileInput(attrs={
                'id': 'resumeInput',
                'class': 'file-input',
            }),
        }
