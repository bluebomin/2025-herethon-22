from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'desired_job', 'desired_region', 'start_year', 'end_year', 'career_gap_years']
    search_fields = ['title', 'company']
    list_filter = ['desired_job', 'desired_region']  # 'career' 대신 실제 존재하는 필드명 사용
