from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, User


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



### 底下為 djangorestframework ---------------------
from rest_framework import permissions
from blog.permissions import IsOwnerOrReadOnly
from django.http import Http404 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class UserDetail(APIView):

    def get_object(self, pk): 
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist: 
            raise Http404

    def get(self, request, pk):
        uu = self.get_object(pk)
        serializer = UserSerializer(uu)
        return Response(serializer.data)

    def put(self, request, pk):
        uu = self.get_object(pk)
        serializer = UserSerializer(uu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        uu = self.get_object(pk)
        uu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ArticleList(APIView):

    def get(self, request, format=None):
        users = Article.objects.all()
        serializer = ArticleSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ArticleDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk): 
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist: 
            raise Http404

    def get(self, request, pk):
        uu = self.get_object(pk)
        serializer = ArticleSerializer(uu)
        return Response(serializer.data)

    def put(self, request, pk):
        uu = self.get_object(pk)
        serializer = ArticleSerializer(uu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        uu = self.get_object(pk)
        uu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)