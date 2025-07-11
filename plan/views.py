# views.py (plan 앱의 views.py)

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
        plan = request.user.plan  # 기존 플랜이 있으면 가져옴
    except Plan.DoesNotExist:
        plan = None  # 없으면 None

    if request.method == 'POST':
        print("=== POST 요청 받음 ===")
        print("Raw POST 데이터:", request.POST)  # 모든 POST 데이터 확인
        print("FILES 데이터:", request.FILES)  # 파일 데이터 확인

        desired_job = request.POST.get('desired_job', '')
        desired_region = request.POST.get('desired_region', '')
        career_gap_years_str = request.POST.get('career_gap_years', '0')
        strengths_str = request.POST.get('strengths', '[]')  # 기본값 '[]' 문자열

        resume = request.FILES.get('resume')
        goal = request.POST.get('goal', '')

        print("\n=== 개별 필드 데이터 확인 ===")
        print(f"desired_job: '{desired_job}'")
        print(f"desired_region: '{desired_region}'")
        print(f"career_gap_years (raw): '{career_gap_years_str}'")
        print(f"strengths (raw): '{strengths_str}'")
        print(f"resume: {resume}")
        print(f"goal: '{goal}'")

        # career_gap_years 처리
        try:
            career_gap_years = int(career_gap_years_str)
        except ValueError:
            career_gap_years = 0
            print(f"경고: career_gap_years '{career_gap_years_str}'가 유효한 숫자가 아닙니다.")

        # strengths JSON 파싱
        parsed_strengths = []
        if strengths_str:
            try:
                parsed_strengths = json.loads(strengths_str)
                if not isinstance(parsed_strengths, (list, dict)):
                    print(f"경고: strengths가 JSON 리스트/딕셔너리가 아님. 초기화.")
                    parsed_strengths = []
            except json.JSONDecodeError:
                print(f"경고: strengths JSON 파싱 실패. 초기화.")
                parsed_strengths = []

        print(f"계산된 career_gap_years: {career_gap_years}")
        print(f"파싱된 strengths: {parsed_strengths}")

        try:
            if plan:  # 기존 Plan 업데이트
                plan.desired_job = desired_job
                plan.desired_region = desired_region
                plan.career_gap_years = career_gap_years
                plan.strengths = parsed_strengths
                if resume:
                    plan.resume = resume
                plan.goal = goal
                plan.save()
                print("=== 기존 Plan 업데이트 완료 ===")
            else:  # 새 Plan 생성
                plan = Plan.objects.create(
                    user=request.user,
                    desired_job=desired_job,
                    desired_region=desired_region,
                    career_gap_years=career_gap_years,
                    strengths=parsed_strengths,
                    resume=resume,
                    goal=goal
                )
                print("=== 새 Plan 생성 완료 ===")
            print(f"최종 저장된 Plan ID: {plan.id}")

        except Exception as e:
            import traceback
            traceback.print_exc()
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
            pass

    desired_job = request.GET.get('desired_job', '')
    desired_region = request.GET.get('desired_region', '')
    career_gap_years = request.GET.get('career_gap_years', 0)

    context = {
        'plan': plan,
        'desired_job': desired_job,
        'desired_region': desired_region,
        'career_gap_years': career_gap_years,
    }
    return render(request, 'plan/plan_recommend.html', context)
