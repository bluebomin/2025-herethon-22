from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PlanForm
from .models import Plan

@login_required
def plan_create_or_update(request):
    try:
        plan = request.user.plan  # OneToOne 관계
    except Plan.DoesNotExist:
        plan = None

    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.user = request.user
            new_plan.save()
            return redirect('post:post_list')  # 작성 후 돌아갈 페이지
    else:
        form = PlanForm(instance=plan)

    return render(request, 'plan/plan_form.html', {'form': form})
