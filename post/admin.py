from django.contrib import admin
<<<<<<< HEAD
from .models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'career', 'career_years', 'link']
    search_fields = ['title', 'company']
    list_filter = ['career']
=======
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
>>>>>>> 3a3d1a26dcd817d2f8e03b9fe11d15700a27b807
