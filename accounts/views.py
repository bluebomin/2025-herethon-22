from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공!')
            return redirect('home')  
        else:
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('home')  # 홈 페이지로 리다이렉트

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        print('회원가입 성공!')
        return redirect('login')  # 로그인 페이지로 리다이렉트
    else:
        return render(request, 'signup.html')