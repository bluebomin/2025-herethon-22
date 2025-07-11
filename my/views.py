from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plan.models import Plan 
from jobs.models import Bookmark, JobPost 
from django.contrib.auth.models import User

@login_required
def myprofile(request):
    my_plan = None
    try:
        my_plan = request.user.plan 
    except Plan.DoesNotExist:
        pass

    all_bookmark = Bookmark.objects.filter(user=request.user) #
    strengths =3 ;

    context = {
        'my_plan': my_plan,
        'strengths_count' : strengths,
        'bookmarks': all_bookmark
    }
    return render(request, 'mypage.html', context)