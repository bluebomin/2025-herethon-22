<<<<<<< HEAD:jobs/urls.py
from django.contrib import admin
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('job_list/', views.job_list, name = 'job_list'),
    path('jobs/<int:pk>/go/', views.redirect_to_job_link, name="job_redirect"),
]
=======
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 게시글 목록
    path('write/', views.post_create, name='post_create'),  # 게시글 작성
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 게시글 상세
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),  # 댓글 작성
]
>>>>>>> 258620bc936f5c32545501e9a3bf71bcce813ee4:post/urls.py
