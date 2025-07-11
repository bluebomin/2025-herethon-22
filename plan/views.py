from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PlanForm
from .models import Plan
from django.urls import reverse
from urllib.parse import urlencode

@login_required
def plan_create_or_update(request):
    try:
        plan = request.user.plan
    except Plan.DoesNotExist:
        plan = None

    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.user = request.user
            new_plan.save()
            # GET 파라미터로 값 전달
            params = urlencode({
                'desired_job': new_plan.desired_job,
                'desired_region': new_plan.desired_region,
                'career_gap_years': new_plan.career_gap_years,
                # 필요시 추가
            })
            url = reverse('plan:plan_recommend') + f'?{params}'
            return redirect(url)
    else:
        form = PlanForm(instance=plan)

    return render(request, 'plan/plan_form.html', {'form': form})

def plan_recommend(request):
    context = {
        'desired_job': request.GET.get('desired_job', ''),
        'desired_region': request.GET.get('desired_region', ''),
        'career_gap_years': request.GET.get('career_gap_years', ''),
    }
    return render(request, 'plan/plan_recommend.html', context)
