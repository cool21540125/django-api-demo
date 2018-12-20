# Django123

- 2018/12/20


## 0. 建立環境

PASS

## 1. 建立 Django 專案

```sh
### 安裝套件
$ pip install django==1.11
$ pip install djangorestframework

### 凍結套件包
$ pip freeze > requirements.txt

### 依照指定檔案安裝套件
$ pip install -r requirements.txt

### 起始 Django 專案
$ django-admin startproject proj

### 開始 run 專案
$ cd proj
$ python manage.py runserver
# http://127.0.0.1:8000
```

## 2. 專案架構介紹

PASS

## 3. 建立 Application

```sh
### 建立 blog 這個應用程式
$ python manage.py startapp blog
```