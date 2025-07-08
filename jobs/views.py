from django.shortcuts import render, redirect
from django.db.models import Q
from .models import JobPost
from .forms import JobPostForm
# Create your views here.
def job_list(request):
    query = request.GET.get('q')
    career_filters = request.GET.getlist('career_filter')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')

    jobs = JobPost.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)

    if 'total' not in career_filters:
        career_q = Q()

        if 'new' in career_filters:
            career_q |= Q(career='신입')
        if 'none' in career_filters:
            career_q |= Q(career="없음 ")
        if 'exp' in career_filters and min_year and max_year:
            try:
                min_y = int(min_year)
                max_y = int(max_year)
                career_q |= Q(career='경력', career_years__gte=min_y, career_years__lte=max_y)
            except ValueError:
                pass
        
        jobs = jobs.filter(career_q)
    return render(request, 'job_list.html', {'jobs': jobs}) #html 이름 다를 시 변경

def create(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = JobPostForm()
    return render(request, 'form_create.html',{'form':form})
