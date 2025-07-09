from django.contrib import admin
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('job_list/', views.job_list, name = 'job_list'),
    path('jobs/<int:pk>/go/', views.redirect_to_job_link, name="job_redirect"),
    path('bookmark/<int:job_post_id>/toggle/', views.toggle_bookmark, name='toggle_bookmark')
]