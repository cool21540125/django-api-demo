# Django123

- 2018/12/20


## 0. 建立環境

PASS


## 1. 建立 Django 專案

```sh
### 安裝套件
$ pip install django==1.11

### 凍結套件包
$ pip freeze > requirements.txt

### 依照指定檔案安裝套件
$ pip install -r requirements.txt

### 起始 Django 專案
$ django-admin startproject proj

### 開始 run 專案
$ cd proj         # 第一層 /proj/ 裡面
$ python manage.py runserver
# http://127.0.0.1:8000
# Ctrl + C 中斷
```


## 2. 專案架構介紹

PASS


## 3. 建立 Application

```sh
### 建立 blog 這個應用程式
$ python manage.py startapp blog

### 修改 /proj/proj/settings.py (註冊應用程式到 Django 主專案)
# 在 INSTALLED_APPS 區塊增加 「blog」這個應用程式

### 修改 /proj/proj/urls.py (Django主專案 路由機制 交由 App路由機制自行管控)
# 1. 修改第一行為 「from django.conf.urls import url, include」
# 2. 在 urlpatterns 裏頭新增 「url(r'^blog/', include('blog.urls')),」

### 新增並修改 /proj/blog/urls.py (App路由機制)
# -------------------- 內容如下 --------------------
from django.conf.urls import url
from . import views

urlpatterns = [
    # 路徑用法使用 Regular Expression
    url(r'^$', views.page0),    # 訪問 /blog
    url(r'1$', views.page1),    # 訪問 /blog/1
    url(r'2$', views.page2),    # 訪問 /blog/2
]
# -------------------- 內容如上 --------------------

### 修改 /proj/blog/views.py
# -------------------- 內容如下 --------------------
from django.shortcuts import render
from django.http import HttpResponse

# 回傳字串的用法
def page0(request):
    return HttpResponse("這是 http://127.0.0.1:8000/blog/")

# 回傳網頁的用法
def page1(request):
    return render(request, 'blog/page1.html')

# 回傳網頁, 並且夾帶後端資料的用法
def page2(request):
    return render(request, 'blog/page2.html', {'name': 'tony', 'projerty': 'smart'})
# -------------------- 內容如上 --------------------
```

### Python 基本觀念補充

```sh
# Python 專案架構如下:
/proj
    /app1.py
    /app2.py
```
如果 /proj/app1.py 想要使用 /proj/app2.py 裡面的東西的話

則需要再 /proj 裡面新增一個「__init__.py」的檔案(可為空檔案), 如此一來

* 「/proj」則變成 Python 合法的 package; 
* 「/proj/app1.py」 則變成 Python 合法的 Module

```sh
# 變成這樣
/proj
    /__init__.py
    /app1.py
    /app2.py
```



## 4. 業務邏輯

### Models: 一個作者可以發文, 改文, 刪文

```sh
### 修改 /proj/blog/models.py
# -------------------- 內容如下 --------------------
from django.db import models

class Article(models.Model):
    author = models.ForeignKey('User', related_name='author_name')
    title = models.CharField(max_length=20)
    context = models.TextField(blank=True, default='')
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name
# -------------------- 內容如上 --------------------
```


### Database

```sh
### 製作 /proj/blog/migrations/ 紀錄
$ python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article
    - Create model User
    - Add field author to article

### 將上述 migrations 裏頭最新的Schema紀錄, 同步到 database
$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
```

### 測試文件

```sh
### 新增 api.http
@baseURL=127.0.0.1:8000

### 
GET http://{{baseURL}}/blog

### 
GET http://{{baseURL}}/blog/1

### 
GET http://{{baseURL}}/blog/2
```




## 5. DjangoRestFramework

* https://www.django-rest-framework.org/tutorial/quickstart/

```sh
### Django REST 套件
$ pip install djangorestframework
```


