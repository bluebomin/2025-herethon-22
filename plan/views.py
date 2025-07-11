from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PlanForm
from .models import Plan
from django.urls import reverse
from urllib.parse import urlencode
import json
from django.core.exceptions import ValidationError

@login_required
def plan_create_or_update(request):
    try:
        plan = request.user.plan
    except Plan.DoesNotExist:
        plan = None

    if request.method == 'POST':
        print("=== POST 요청 받음 ===")
        print("POST 데이터:", request.POST)
        print("FILES 데이터:", request.FILES)

        # 다중 선택값 처리
        desired_job = request.POST.get('desired_job', '')
        desired_region = request.POST.get('desired_region', '')
        desired_job_list = [v for v in desired_job.split(',') if v]
        desired_region_list = [v for v in desired_region.split(',') if v]
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        strengths = request.POST.get('strengths', '[]')
        resume = request.FILES.get('resume')
        goal = request.POST.get('goal', '')

        print("받은 데이터:")
        print(f"desired_job: {desired_job_list}")
        print(f"desired_region: {desired_region_list}")
        print(f"start_year: {start_year}")
        print(f"end_year: {end_year}")
        print(f"strengths: {strengths}")
        print(f"goal: {goal}")

        if not desired_job_list or not desired_region_list:
            print("=== 필수 필드 누락 ===")
            print(f"desired_job: '{desired_job_list}'")
            print(f"desired_region: '{desired_region_list}'")
            return render(request, 'plan/plan_form.html', {'error': '필수 필드를 입력해주세요.'})

        # Plan 객체 생성/수정
        if plan:
            plan.desired_job = desired_job_list
            plan.desired_region = desired_region_list
            plan.start_year = int(start_year) if start_year else None
            plan.end_year = int(end_year) if end_year else None
            try:
                plan.strengths = json.loads(strengths)
            except:
                plan.strengths = []
            if resume:
                plan.resume = resume
            plan.goal = goal
        else:
            plan = Plan(
                user=request.user,
                desired_job=desired_job_list,
                desired_region=desired_region_list,
                start_year=int(start_year) if start_year else None,
                end_year=int(end_year) if end_year else None,
                strengths=json.loads(strengths) if strengths else [],
                resume=resume,
                goal=goal
            )
        try:
            plan.full_clean()  # clean() 호출
            plan.save()
            print("=== Plan 저장 완료 ===")
        except ValidationError as e:
            print(f"=== 유효성 검증 에러: {e} ===")
            return render(request, 'plan/plan_form.html', {'form': PlanForm(instance=plan), 'errors': e.messages})

        print("=== 저장 완료, redirect 시작 ===")
        params = urlencode({
            'desired_job': ','.join(desired_job_list),
            'desired_region': ','.join(desired_region_list),
            'career_gap_years': plan.career_gap_years,
        })
        url = reverse('plan:plan_recommend') + f'?{params}'
        print(f"redirect URL: {url}")
        return redirect(url)

    else:
        print("=== GET 요청 ===")
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
