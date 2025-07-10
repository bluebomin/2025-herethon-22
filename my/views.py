from django.shortcuts import render
from plan.models import Plan
# Create your views here.
def myprofile(request):
    context = {
        
    }
    return render(request, 'myprofile.html', context)