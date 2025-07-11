from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PlanForm
from .models import Plan
from django.urls import reverse
from urllib.parse import urlencode
import json

@login_required
def plan_create_or_update(request):
    try:
        plan = request.user.plan
    except Plan.DoesNotExist:
        plan = None

    if request.method == 'POST':
        # 순수 HTML input에서 데이터 받기
        desired_job = request.POST.get('desired_job', '')
        desired_region = request.POST.get('desired_region', '')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        strengths = request.POST.get('strengths', '[]')
        resume = request.FILES.get('resume')
        goal = request.POST.get('goal', '')

        # 데이터 검증
        if not desired_job or not desired_region:
            # 에러 처리
            return render(request, 'plan/plan_form.html', {'error': '필수 필드를 입력해주세요.'})

        # Plan 객체 생성 또는 업데이트
        if plan:
            # 기존 Plan 업데이트
            plan.desired_job = desired_job
            plan.desired_region = desired_region
            if start_year and end_year:
                plan.start_year = int(start_year)
                plan.end_year = int(end_year)
                plan.career_gap_years = int(end_year) - int(start_year)
            try:
                plan.strengths = json.loads(strengths)
            except:
                plan.strengths = []
            if resume:
                plan.resume = resume
            plan.goal = goal
            plan.save()
        else:
            # 새 Plan 생성
            plan = Plan.objects.create(
                user=request.user,
                desired_job=desired_job,
                desired_region=desired_region,
                start_year=int(start_year) if start_year else None,
                end_year=int(end_year) if end_year else None,
                career_gap_years=int(end_year) - int(start_year) if start_year and end_year else 0,
                strengths=json.loads(strengths) if strengths else [],
                resume=resume,
                goal=goal
            )

        # 성공 시 recommend 페이지로 이동
        params = urlencode({
            'desired_job': plan.desired_job,
            'desired_region': plan.desired_region,
            'career_gap_years': plan.career_gap_years,
        })
        url = reverse('plan:plan_recommend') + f'?{params}'
        return redirect(url)
    else:
        # GET 요청 시 기존 데이터가 있으면 폼에 표시
        form = PlanForm(instance=plan) if plan else PlanForm()

    return render(request, 'plan/plan_form.html', {'form': form})

def plan_recommend(request):
    plan = None
    if request.user.is_authenticated:
        try:
            plan = request.user.plan
        except Plan.DoesNotExist:
            plan = None
    context = {
        'plan': plan,
    }
    return render(request, 'plan/plan_recommend.html', context)
