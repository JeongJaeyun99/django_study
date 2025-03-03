from django.urls import path
from . import views

app_name = 'users'  # alias 설정  패키지이름과 똑같이 한다
urlpatterns = [
    # 모든 사용자 조회
    path('', views.get_all_users, name='users:get_all_users'),
    # 사용자 생성
    path('create/', views.create_user, name='users:create_user'),
    # ID로 사용자 조회
    path('<int:id>/', views.get_user_by_id, name='users:get_user_by_id'),
    # 사용자 이름으로 조회
    path('name/<str:name>/', views.get_users_by_name, name='users:get_users_by_name'),
    # 특정 나이 이상의 사용자 조회
    path('age_gte/<int:age>/', views.get_users_by_age_gte, name='users:get_users_by_age_gte'),
    # 사용자 삭제
    path('delete/<int:id>/', views.delete_user_by_id, name='users:delete_user_by_id'),
]