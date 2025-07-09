from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.
def myprofile(request):
    profile_form = ProfileForm()
    context = {
        'profileform' : profile_form
    }
    return render(request, 'myprofile.html', context)