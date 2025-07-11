from django.urls import path
from . import views

app_name = 'alumna'

urlpatterns = [
    path('', views.alumna_list, name='alumna_list'),
    path('write/', views.alumna_create, name='alumna_create'),
    path('<int:pk>/', views.alumna_detail, name='alumna_detail'),
    path('<int:pk>/comment/', views.alumna_comment_create, name='alumna_comment_create'),
]
