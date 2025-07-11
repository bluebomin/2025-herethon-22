from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('myplan/', views.plan_create_or_update, name='myplan'),
    path('recommend/', views.plan_recommend, name='plan_recommend'),
]
