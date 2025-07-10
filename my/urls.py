from django.urls import path
from . import views

app_name="my"

urlpatterns = [
    path('mypage',views.myprofile, name='mypage')
]
