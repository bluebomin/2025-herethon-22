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
        plan = request.user.plan # 기존 플랜이 있으면 가져옴
    except Plan.DoesNotExist:
        plan = None # 없으면 None

    if request.method == 'POST':
        print("=== POST 요청 받음 ===")
        print("Raw POST 데이터:", request.POST) # 모든 POST 데이터 확인
        print("FILES 데이터:", request.FILES) # 파일 데이터 확인

        desired_job = request.POST.get('desired_job', '')
        desired_region = request.POST.get('desired_region', '')
        start_year_str = request.POST.get('start_year') # 문자열로 받음
        end_year_str = request.POST.get('end_year')   # 문자열로 받음
        strengths_str = request.POST.get('strengths', '[]') # 기본값 '[]' 문자열

        resume = request.FILES.get('resume')
        goal = request.POST.get('goal', '')

        print("\n=== 개별 필드 데이터 확인 ===")
        print(f"desired_job: '{desired_job}'")
        print(f"desired_region: '{desired_region}'")
        print(f"start_year (raw): '{start_year_str}'")
        print(f"end_year (raw): '{end_year_str}'")
        print(f"strengths (raw): '{strengths_str}'")
        print(f"resume: {resume}")
        print(f"goal: '{goal}'")

        # start_year와 end_year 처리: 유효한 숫자가 아니면 None으로 설정
        start_year = None
        end_year = None
        if start_year_str:
            try:
                start_year = int(start_year_str)
            except ValueError:
                print(f"경고: start_year '{start_year_str}'가 유효한 숫자가 아닙니다.")
        if end_year_str:
            try:
                end_year = int(end_year_str)
            except ValueError:
                print(f"경고: end_year '{end_year_str}'가 유효한 숫자가 아닙니다.")

        # career_gap_years 계산 (Null 또는 유효하지 않은 경우를 대비)
        career_gap_years = 0
        if start_year is not None and end_year is not None and end_year >= start_year:
            career_gap_years = end_year - start_year
        else:
            print(f"경고: 경력 단절 연도 계산 불가 (start_year: {start_year}, end_year: {end_year})")


        # strengths JSON 파싱: 유효하지 않으면 빈 리스트 또는 기본값으로 설정
        parsed_strengths = []
        if strengths_str: # 빈 문자열이 아니면 시도
            try:
                parsed_strengths = json.loads(strengths_str)
                # JSONField는 리스트나 딕셔너리여야 함. HTML input에서 넘어온 값은 문자열일 수 있음.
                if not isinstance(parsed_strengths, (list, dict)):
                    print(f"경고: strengths '{strengths_str}'가 유효한 JSON 리스트/딕셔너리가 아닙니다. 빈 리스트로 초기화합니다.")
                    parsed_strengths = []
            except json.JSONDecodeError:
                print(f"경고: strengths '{strengths_str}'가 유효한 JSON 형식이 아닙니다. 빈 리스트로 초기화합니다.")
                parsed_strengths = []
        
        print(f"계산된 career_gap_years: {career_gap_years}")
        print(f"파싱된 strengths (JSON): {parsed_strengths}")

        try:
            if plan: # 기존 플랜이 있으면 업데이트
                plan.desired_job = desired_job
                plan.desired_region = desired_region
                plan.career_gap_years = career_gap_years
                plan.start_year = start_year 
                plan.end_year = end_year
                plan.strengths = parsed_strengths
                if resume: 
                    plan.resume = resume
                plan.goal = goal
                plan.save()
                print("=== 기존 Plan 업데이트 완료 ===")
            else: 
                plan = Plan.objects.create(
                    user=request.user,
                    desired_job=desired_job,
                    desired_region=desired_region,
                    career_gap_years=career_gap_years,
                    start_year=start_year, 
                    end_year=end_year,
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