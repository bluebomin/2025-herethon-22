from django import forms
from .models import CounselPost, CounselComment

class CounselPostForm(forms.ModelForm):
    class Meta:
        model = CounselPost
        fields = ['title', 'content']

class CounselCommentForm(forms.ModelForm):
    class Meta:
        model = CounselComment
        fields = ['content']
