from django.urls import path
from .views import hello # .은 부모

urlpatterns = [
   path('book/', hello,name = 'hello'), # 'book/' 장고는 /는 뒤로와야함 path(request하는곳,response하는곳)
]
