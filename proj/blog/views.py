from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# 回傳字串的用法
def page0(request):
    return HttpResponse("這是 http://127.0.0.1:8000/blog/")

# 回傳網頁的用法
def page1(request):
    return render(request, 'blog/page1.html')

# 回傳網頁, 並且夾帶後端資料的用法
def page2(request):
    return render(request, 'blog/page2.html', {'name': 'tony', 'projerty': 'smart'})

# Django CRUD
def users(request):
    if request.method == 'GET':
        return HttpResponse('GET')
    elif request.method == 'POST':
        return HttpResponse('POST')
    elif request.method == 'PUT':
        return HttpResponse('PUT')
    elif request.method == 'DELETE':
        return HttpResponse('DELETE')


