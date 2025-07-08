from django import forms
<<<<<<< HEAD:jobs/forms.py
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'

=======
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
>>>>>>> 258620bc936f5c32545501e9a3bf71bcce813ee4:post/forms.py
