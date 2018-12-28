from django.contrib import admin
from django.conf.urls import url, include
from . import view

#项目的url
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'hello/', view.hello),
    url(r'^', include('booktest.urls')), #模块url
]
