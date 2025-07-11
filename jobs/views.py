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
    job_type_filter = request.GET.getlist('job_type_filter') 
    if job_type_filter:
        jobs = jobs.filter(job_type__in=job_type_filter)
    
    #3. 지역 필터
    region_filter = request.GET.getlist('region_filter') 
    if region_filter:
        jobs = jobs.filter(region__in=region_filter)
    
    #4. 재택 가능 여부
    remote_available_filter = request.GET.get('remote_available_filter') 
    if remote_available_filter in ['true', 'True', '1', 'on']:
        jobs = jobs.filter(remote_available=True) 
    
    #5. 경력 필터
    career_filters_selected = request.GET.getlist('career_filter')
    start_year_input = request.GET.get('start_year')
    end_year_input = request.GET.get('end_year')

    career_q = Q()
    
    
    if 'total' in career_filters_selected or not career_filters_selected:
        pass 
    else:        
        if 'new' in career_filters_selected:
            career_q |= Q(career='new')
        if 'none' in career_filters_selected:
            career_q |= Q(career="none")
            
        if 'exp' in career_filters_selected:
            try:
                start_year_val = int(start_year_input)
                end_year_val = int(end_year_input)

                if start_year_val <= end_year_val:
                    required_exp_years = end_year_val - start_year_val
                    career_q |= Q(career='exp', career_years=required_exp_years) 
                    
                else:                
                    print("경력 시작 연도는 종료 연도보다 클 수 없습니다.")
                    
            except ValueError:
                print("유효하지 않은 연도 형식입니다.")
                
            
        jobs = jobs.filter(career_q)
    
    #6. 학력 필터
    education_filter = request.GET.getlist('education_filter') 
    if education_filter:
        jobs = jobs.filter(education__in=education_filter) 

    #7. 기업 규모 필터
    company_size_filter = request.GET.getlist('company_size_filter') 
    if company_size_filter:
        jobs = jobs.filter(company_size__in=company_size_filter) 
    
    #북마크
    user_bookmarked_job_ids = []
    if request.user.is_authenticated:
        user_bookmarked_job_ids = request.user.bookmark_set.all().values_list('job_post_id', flat=True)
    
    context = {
        'jobs':jobs,
        'career_filters_selected': career_filters_selected,
        'user_bookmarked_job_ids': list(user_bookmarked_job_ids),

    }
    return render(request, 'job_list.html', context) 



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