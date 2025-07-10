from django.contrib import admin
from .models import JobPost, Bookmark

# Register your models here.
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'career', 'career_years', 'link']
    search_fields = ['title', 'company']
    list_filter = ['career']

admin.site.register(Bookmark)