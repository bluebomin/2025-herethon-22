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
        print("=== POST 요청 받음 ===")
        print("POST 데이터:", request.POST)
        print("FILES 데이터:", request.FILES)

        # 순수 HTML input에서 데이터 받기
        desired_job = request.POST.get('desired_job', '')
        desired_region = request.POST.get('desired_region', '')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        strengths = request.POST.get('strengths', '[]')
        resume = request.FILES.get('resume')
        goal = request.POST.get('goal', '')

        print("받은 데이터:")
        print(f"desired_job: {desired_job}")
        print(f"desired_region: {desired_region}")
        print(f"start_year: {start_year}")
        print(f"end_year: {end_year}")
        print(f"strengths: {strengths}")
        print(f"goal: {goal}")

        if not desired_job or not desired_region:
            print("=== 필수 필드 누락 ===")
            print(f"desired_job: '{desired_job}'")
            print(f"desired_region: '{desired_region}'")
            return render(request, 'plan/plan_form.html', {'error': '필수 필드를 입력해주세요.'})

        try:
            if plan:
                print("=== 기존 Plan 업데이트 ===")
                plan.desired_job = desired_job
                plan.desired_region = desired_region
                if start_year and end_year:
                    plan.career_gap_years = int(end_year) - int(start_year)
                try:
                    plan.strengths = json.loads(strengths)
                except:
                    plan.strengths = []
                if resume:
                    plan.resume = resume
                plan.goal = goal
                plan.save()
                print("=== 기존 Plan 저장 완료 ===")
            else:
                print("=== 새 Plan 생성 ===")
                plan = Plan.objects.create(
                    user=request.user,
                    desired_job=desired_job,
                    desired_region=desired_region,
                    career_gap_years=int(end_year) - int(start_year) if start_year and end_year else 0,
                    strengths=json.loads(strengths) if strengths else [],
                    resume=resume,
                    goal=goal
                )
                print("=== 새 Plan 생성 완료 ===")
                print(f"생성된 Plan ID: {plan.id}")
        except Exception as e:
            print(f"=== 데이터베이스 저장 에러: {e} ===")
            return render(request, 'plan/plan_form.html', {'error': f'저장 중 오류가 발생했습니다: {e}'})

        print("=== 저장 완료, redirect 시작 ===")
        params = urlencode({
            'desired_job': plan.desired_job,
            'desired_region': plan.desired_region,
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
