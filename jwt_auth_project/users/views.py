from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny 
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken 
from .serializers import SignupSerializer 

# Create your views here.

class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            refresh = RefreshToken(refresh_token)
            return Response({'access':str(refresh.access_token)}, status = status.HTTP_200_OK)
        except Exception as e: 
            return Response({'error':'INVALID_REFRESH_TOKEN'}, status = status.HTTP_400_BAD_REQUEST)

# 회원가입 api (유효성 검사 전)
# class SignupView(APIView):
#     permission_classes = [AllowAny] # AllowAny를 사용하면 이 api는 모든 사용자(인증되지 않은 사용자 포함)에게 공개됨. 

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         nickname = request.data.get('nickname')

#         if get_user_model().objects.filter(username=username).exists():
#             return Response({"error": {"code":"USER_ALREADY_EXISTS", "message":"이미 가입된 사용자입니다."}},
#                             status = status.HTTP_400_BAD_REQUEST)
        
#         # 유저 생성 로직 
#         user = get_user_model().objects.create_user(username = username, password = password, nickname = nickname)
#         # return Response({'username':username,
#         #                  'password':password,},
#         #                 status = status.HTTP_201_CREATED)
#         return Response(request.data,
#                         status = status.HTTP_201_CREATED)


# 회원가입 api (유효성 검사 추가)
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save() # 자동으로 데이터베이스에 저장
            return Response(request.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)





# 로그인 api 
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_object_or_404(get_user_model(), username = username)

        if not user.check_password(password):
            return Response({'error':{'code':'INVALID_CREDENTIALS', 'message':'아이디 또는 비밀번호가 올바르지 않습니다.'}},
                            status = status.HTTP_401_UNAUTHORIZED)
        
        token = RefreshToken.for_user(user).access_token #JWT 토큰 생성 
        return Response({'token':str(token)}, status = status.HTTP_200_OK)
