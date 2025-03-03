from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Books
from .serializer import BookSerializer


# 모든 책 조회
@api_view(['GET'])
def get_all_books(request):
   books = Books.objects.all()
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 책 생성
@api_view(['POST'])
def create_book(request):
   serializer = BookSerializer(data=request.data) # 직렬화를 시켜서 혹시모를 리액트에서의 오류를 없앰("" 때문)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # ID로 책 조회
# @api_view(['GET'])
# def get_book_by_id(request, id):
#    try:
#        book = Books.objects.get(id=id)
#        serializer = BookSerializer(book)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    except Books.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

# 책 이름으로 조회
@api_view(['GET'])
def get_books_by_title(request, title):
   books = Books.objects.filter(title=title) # where 절
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 작가로 책 조회
@api_view(['GET'])
def get_books_by_author(request, author):
   books = Books.objects.filter(author = author)
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 출판사로 책 조회
@api_view(['GET'])
def get_books_by_publisher(request, publisher):
   books = Books.objects.filter(publisher = publisher)
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 삭제
@api_view(['DELETE'])
def delete_book_by_id(request, id):
   try:
       book = Books.objects.get(id=id)
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Books.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

