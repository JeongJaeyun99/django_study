from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Orders
from .serializer import OrderSerializer


# 모든 주문 조회
@api_view(['GET'])
def get_all_orders(request):
   orders = Orders.objects.all()
   serializer = OrderSerializer(orders, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 주문 생성 고쳐야함!
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data) # 직렬화를 시켜서 혹시모를 리액트에서의 오류를 없앰("" 때문)
    if serializer.is_valid():
        # print("data : ", serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ID로 주문 조회
@api_view(['GET'])
def get_order_by_id(request, id):
   try:
       order = Orders.objects.get(id=id)
       serializer = OrderSerializer(order)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except Orders.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 사용자 id로 주문 조회
@api_view(['GET'])
def get_orders_by_user_id(request, user_id):
   orders = Orders.objects.filter(user_id=user_id) # where 절
   serializer = OrderSerializer(orders, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 책 id로 주문 조회
@api_view(['GET'])
def get_orders_by_book_id(request, book_id):
   orders = Orders.objects.filter(book_id=book_id) # where 절
   serializer = OrderSerializer(orders, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 삭제
@api_view(['DELETE'])
def delete_order_by_id(request, id):
   try:
       order = Orders.objects.get(id=id)
       order.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Orders.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
