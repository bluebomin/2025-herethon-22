from .models import MyProfile
from django import forms 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ['']