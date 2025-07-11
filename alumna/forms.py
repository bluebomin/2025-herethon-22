from django import forms
from .models import AlumnaPost, AlumnaComment

class AlumnaPostForm(forms.ModelForm):
    class Meta:
        model = AlumnaPost
        fields = ['title', 'content']

class AlumnaCommentForm(forms.ModelForm):
    class Meta:
        model = AlumnaComment
        fields = ['content']
