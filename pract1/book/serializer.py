from rest_framework import serializers
from .models import Books

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = Books
       fields = ['id', 'title', 'author', 'publisher',"price"]