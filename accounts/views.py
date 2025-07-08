# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db import IntegrityError

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
        repeat_password = request.POST['repeat'] 
        email = request.POST['email'] 
        
        # 1. 비밀번호 일치 여부 확인
        if password != repeat_password:
            error_message = "비밀번호가 일치하지 않습니다."
            return render(request, 'signup.html', {
                'error': error_message, 
                'username': username, 
                'email': email 
            })
        
        try:
            # 2. 사용자 생성 시도
            new_user = User.objects.create_user(
                username=username,
                password=password,
                email=email 
            )
            
            print(f'회원가입 성공: {new_user.username}')
            return redirect('accounts:login') # 성공적으로 생성된 경우에만 리다이렉트
            
        except IntegrityError:
            # 3. 중복 아이디 처리
            error_message = "이미 존재하는 아이디입니다."
            return render(request, 'signup.html', {
                'error': error_message, 
                'username': username, 
                'email': email
            })
        except Exception as e:
            # 4. 그 외 예상치 못한 오류 처리
            error_message = f"회원가입 중 예상치 못한 오류가 발생했습니다: {e}"
            print(error_message)
            return render(request, 'signup.html', {
                'error': error_message, 
                'username': username, 
                'email': email
            })
    else:
        # GET 요청일 경우
        return render(request, 'signup.html')