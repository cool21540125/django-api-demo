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


## 2. 專案架構介紹 && 主要指令

### 2-1. 專案架構

```sh
/proj
    /blog       # Django Application
        /__init__.py
        /admin.py       # (我還沒用過)
        /apps.py        # (我還沒用過)
        /models.py      # App Models
        /tests.py       # App 測試
        /urls.py        # App 路由機制
        /views.py       # App views
    /proj       # 專案主檔目錄
        /__init__.py
        /settings.py    # 所有專案設定檔
        /urls.py        # 專案路由機制
        /wsgi.py        # WSGI Application
    /manage.py  # Django CLI 控制檔案
```

### 2-2. 主要指令

```sh
# 先進入第一層 /proj 裡面 (有 manage.py 的地方)
### 起始 Debug Server
python manage.py runserver

### 進入 REPL
python manage.py shell

### 初始化 Database
python manage.py migrate

### 依照 models 作 變更紀錄
python manage.py makemigrations <AppName>

### 建立 Django admin user
python manage.py createsuperuser --username <UserName> --email <EMail>

# python manage.py migrate
# python manage.py makemigrations blog
# python manage.py migrate
# python manage.py createsuperuser --username tony --email cool21540125@gmail.com
```


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
### 依照 models 紀錄, 更新 Database
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
# 上面這堆, 是在建立 table


### 依照 models 作變更紀錄
$ python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article
# 建立 /proj/blog/migrations/...
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


## 5. Django Shell

Django 可以使用互動式介面來作除錯...

```sh
$ python manage.py shell

# 匯入 models 裏頭的物件, 使用 ORM 語法對物件模型作操作
>>> from blog.models import *

# ORM 語法作查詢
>>> User.objects.all()
<QuerySet []>

>>> u1 = User.objects.first()

# 新增一位使用者
>>> s = User.objects.create(username='scott')
>>> s.set_password('scott123')
>>> s.save()

# 新增一篇文章
>>> Article.objects.create(title='demo', context='Django manage.py shell 測試', author_id=1)

# 新增第二位使用者
>>> u2 = User.objects.create(name='scott', iq=100)

# 第二位使用者發文
>>> Article.objects.create(title='我是阿良', context='python 弱弱的', author_id=u2.id)
<Article: 我是阿良>

# 第二位使用者發文
>>> Article.objects.create(title='阿良又來了', context='tony好強', author_id=u2.id)
<Article: 阿良又來了>
```

## 6. 

## 7. DjangoRestFramework

* https://www.django-rest-framework.org/tutorial/quickstart/

```sh
### Django REST 套件
$ pip install djangorestframework
```


