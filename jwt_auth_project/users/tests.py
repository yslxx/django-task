from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model 

# Create your tests here.
@pytest.fixture # 설정 함수. 테스트 실행 전에 공통적으로 필요한 데이터를 준비하거나 테스트 환경을 구성하는 데 사용됨. 
def client():
    return APIClient() # 실제 http 요청을 시뮬레이션 함. 
# 테스트 코드에서 api 요청을 보낼 때 사용. 

# @pytest.fixture 
# def create_user():
#     def _create_user(username, password, nickname):
#         return get_user_model().objects.create_user(username = username, password=password, nickname=nickname)
#     return _create_user 

# 회원가입 api 테스트 
def test_signup_success(client):
    response = client.post("/users/signup/", {'username':'jinho', 'password':'12341234', 'nickname':'mentos'},
                           format = 'json')
    assert response.status_code == 201
    assert response.data['username'] == 'jinho'
    print('회원가입 완료', response.data)


# 로그인 api 테스트 
def test_login_success(client):
    # create_user('loginuser', 'testpass', 'nick')
    response = client.post('/users/login/', {'username':'jinho', 'password':'12341234'},
                           format = 'json')
    print('로그인: ', response.data)
    assert response.status_code == 200
    assert 'token' in response.data # 로그인 성공 시 jwt 토큰이 반환되어야 함. 
    print('로그인 완료', response.data)