from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password = data.get('password', '')

            # 입력 검증
            if not username or not password:
                return JsonResponse({'error': '사용자명과 비밀번호를 모두 입력해주세요.'}, status=400)
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': '이미 존재하는 사용자명입니다.'}, status=400)

            user = User.objects.create_user(username=username, password=password)
            auth_login(request, user)  
            return JsonResponse({'message': '회원가입 성공', 'username': user.username})

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': '서버 오류가 발생했습니다.'}, status=500)

    return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=405)

def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password = data.get('password', '')

            # 입력 검증
            if not username or not password:
                return JsonResponse({'error': '사용자명과 비밀번호를 모두 입력해주세요.'}, status=400)

            user = User.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                return JsonResponse({'error': '사용자명 또는 비밀번호가 올바르지 않습니다.'}, status=400)

            auth_login(request, user)
            return JsonResponse({'message': '로그인 성공', 'username': user.username})

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': '서버 오류가 발생했습니다.'}, status=500)

    return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=405)

@login_required
def user_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return JsonResponse({'message': '로그아웃 성공'})

    return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=405)