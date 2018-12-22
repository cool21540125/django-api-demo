from django.conf.urls import url
from . import views

urlpatterns = [
    # 路徑用法使用 Regular Expression
    url(r'^$', views.page0),    # 訪問 /blog
    url(r'1$', views.page1),    # 訪問 /blog/1
    url(r'2$', views.page2),    # 訪問 /blog/2
    url(r'users/$', views.users),
]