from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import JobPost, Bookmark
from .forms import JobPostForm

# Create your views here.
def job_list(request):
    jobs = JobPost.objects.all()

    #1. 제목 검색 필터 
    query = request.GET.get('q')

    if query:
        jobs = jobs.filter(title__icontains=query)
    
    #2. 직종 필터
    job_type_filter = request.GET.get('job_type')
    if job_type_filter:
        jobs = jobs.filter(job_type=job_type_filter)
    
    #3. 지역 필터
    region_filter = request.GET.get('region')
    if region_filter:
        jobs = jobs.filter(region=region_filter)
    
    #4. 재택 가능 여부
    remote_available_filter = request.GET.get('remote_available')
    if remote_available_filter in ['true', 'True', '1']:
        jobs = jobs.filter(remote_available_filter=True)
    
    #5. 경력 필트
    career_filters_selected = request.GET.getlist('career_filter')
    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')

    if 'total' not in career_filters_selected and career_filters_selected:
        career_q = Q()

        if 'new' in career_filters_selected:
            career_q |= Q(career='new')
        if 'none' in career_filters_selected:
            career_q |= Q(career="none ")
        if 'exp' in career_filters_selected and start_year and end_year:
            try:
                start_y = int(start_year)
                end_y = int(end_year)
                exp_years = start_y - end_y
                career_q |= Q(career='exp', career_years__lte = exp_years) #연차를 계산하여 연차보다 같거나 적은 경력 요구 필터링
            except ValueError:
                pass
        
        jobs = jobs.filter(career_q)
    
    #6. 학력 필터
    education_filter = request.GET.get('education')
    if education_filter:
        jobs = jobs.filter(education=education_filter)

    #7. 기업 규모 필터
    company_size_filter = request.GET.get('company_size')
    if company_size_filter:
        jobs = jobs.filter(company_size = company_size_filter)
    
    #북마크
    user_bookmarked_job_ids = []
    if request.user.is_authenticated:
        user_bookmarked_job_ids = request.user.bookmark_set.all().values_list('job_post_id', flat=True)
    
    context = {
        'jobs':jobs,
        'career_filters_selected': career_filters_selected,
        'user_bookmarked_job_ids': list(user_bookmarked_job_ids),

    }
    return render(request, 'job_list.html', context) #html 이름 다를 시 변경



#채용 공고 사이트로 연결
def redirect_to_job_link(request, pk):
    job = get_object_or_404(JobPost, pk=pk)
    if job.link:
        return redirect(job.link)
    else:
        return redirect('job_list')
    
#북마크 토글 뷰 함수
@login_required
def toggle_bookmark(request, job_post_id):
    job_post = get_object_or_404(JobPost, id=job_post_id)

    bookmark, created = Bookmark.objects.get_or_create(user=request.user, job_post=job_post)

    if not created:
        bookmark.delete()
    else:
        pass 
    return redirect(request.META.get('HTTP_REFERER', 'jobs:job_list'))