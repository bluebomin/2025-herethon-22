from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plan.models import Plan
from jobs.models import Bookmark, JobPost
from django.contrib.auth.models import User
# Create your views here.

@login_required
def myprofile(request):
    all_my_profile = Plan.objects.all()
    
    all_bookmark = Bookmark.objects.filter(user=request.user)

    context = {
        'plans':all_my_profile,
        'bookmarks':all_bookmark}
    return render(request, 'mypage.html', context)

