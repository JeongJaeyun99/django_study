from django.urls import path
from . import views

app_name = 'book'  # alias 설정  패키지이름과 똑같이 한다
urlpatterns = [
    # 모든 책 조회
    path('', views.get_all_books, name='book:get_all_books'),
    # 책 생성
    path('create/', views.create_book, name='book:create_book'),
    # # ID로 책 조회
    # path('<int:id>/', views.get_book_by_id, name='book:get_book_by_id'),
    # 책 이름으로 조회
    path('title/<str:title>/', views.get_books_by_title, name='book:get_books_by_title'),
    # 작가 이름으로 사용자 조회
    path('author/<str:author>/', views.get_books_by_author, name='book:get_books_by_author'),
    # 출판사 이름으로 사용자 조회
    path('publisher/<str:publisher>/', views.get_books_by_publisher, name='book:get_books_by_publisher'),
    # 책 삭제
    path('delete/<int:id>/', views.delete_book_by_id, name='book:delete_book_by_id'),
]