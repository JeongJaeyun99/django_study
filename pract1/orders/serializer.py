from rest_framework import serializers
from .models import Orders
from .models import Users
from .models import Books

class OrderSerializer(serializers.ModelSerializer):
    # 모델에서 생성자의 이름인 user,book을 소스로 사용함
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=Users.objects.all())
    book_id = serializers.PrimaryKeyRelatedField(source='book', queryset=Books.objects.all())
    class Meta:
       model = Orders
       fields = ['id', 'user_id', 'book_id', 'address',"price"]