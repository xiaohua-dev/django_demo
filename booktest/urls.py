from django.conf.urls import url
from booktest import views

urlpatterns = [
    #通过url函数设置url路由函数
    url(r'^index', views.index)
]