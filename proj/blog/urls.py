from django.conf.urls import url
from . import views

urlpatterns = [
    # 路徑用法使用 Regular Expression
    url(r'rest_user_list/$', views.UserList.as_view()),
    url(r'rest_user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'rest_article_list/$', views.ArticleList.as_view()),
    url(r'rest_article/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^$', views.page0),    # 訪問 /blog
    url(r'1/$', views.page1),    # 訪問 /blog/1
    url(r'2/$', views.page2),    # 訪問 /blog/2
    url(r'users/$', views.users),
]