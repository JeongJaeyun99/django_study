from django.shortcuts import render # response 하는곳
from django.http import JsonResponse, HttpResponse

# Create your views here.

def hello(request): # ()안의 requset는 request한지 확인하는 역할을 한다.
    data = {
        "tittle" : "Java",
        "author" : "John",
        "publisher" : "제일",
        "price" : 35000
    }
    # return HttpResponse("Hello World")
    return JsonResponse(data)
