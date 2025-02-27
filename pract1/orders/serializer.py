from rest_framework import serializers
from .models import Orders

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = Orders
       fields = ['id', 'user_id', 'book_id', 'address',"price"]