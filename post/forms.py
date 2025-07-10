from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

from django import forms
from .models import Comment

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']
#         labels = {
#             'content': '',
#         }
#         widgets = {
#             'content': forms.TextInput(attrs={
#                 'id': 'myCo',
#                 'placeholder': '댓글로 당신이 알고 있는 정보를 공유해보세요!',
#                 'class': 'my-custom-class',
#             })
#         }
