from django.urls import path
from . import views

app_name = 'orders'  # alias 설정  패키지이름과 똑같이 한다
urlpatterns = [
    # 모든 주문 조회
    path('', views.get_all_orders, name='orders:get_all_orders'),
    # 주문 생성
    path('create/', views.create_order, name='orders:create_order'),
    # ID로 주문 조회
    path('<int:id>/', views.get_order_by_id, name='orders:get_order_by_id'),
    # 특정 사용자의 주문 조회
    path('user_id/<int:user_id>/', views.get_orders_by_user_id, name='orders:get_orders_by_user_id'),
    # 특정 책의 주문 조회
    path('book_id/<int:book_id>/', views.get_orders_by_book_id, name='orders:get_orders_by_book_id'),
    # 주문 삭제
    path('delete/<int:id>/', views.delete_order_by_id, name='orders:delete_order_by_id'),
]
# path('delete/<int:id>/', views.delete_user_by_id, name='users:delete_user_by_id') 예를들자면 <int:id>안에 name='users:delete_user_by_id 이게 쓰인다.