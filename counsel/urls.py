from django.urls import path
from . import views

app_name = 'counsel'

urlpatterns = [
    path('', views.counsel_list, name='counsel_list'),
    path('write/', views.counsel_create, name='counsel_create'),
    path('<int:pk>/', views.counsel_detail, name='counsel_detail'),
    path('<int:pk>/comment/', views.counsel_comment_create, name='counsel_comment_create'),
]
