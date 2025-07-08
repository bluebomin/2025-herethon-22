from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
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
                exp_years = max_y - min_y
                career_q |= Q(career='경력', career_years__lte = exp_years) #연차를 계산하여 연차보다 같거나 적은 경력 요구 필터링
            except ValueError:
                pass
        
        jobs = jobs.filter(career_q)
    return render(request, 'job_list.html', {'jobs': jobs}) #html 이름 다를 시 변경


#관리자만 채용 정보 게시할 수 있게 설정
def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # 생성 후 목록으로 이동
    else:
        form = JobPostForm()

    return render(request, 'create_job_post.html', {'form': form})

#채용 공고 사이트로 연결
def redirect_to_job_link(request, pk):
    job = get_object_or_404(JobPost, pk=pk)
    if job.link:
        return redirect(job.link)
    else:
        return redirect('job_list')