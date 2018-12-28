from django.contrib import admin
#后台管理
from booktest.models import BookInfo

# Register your models here.
#注册类模型

admin.site.register(BookInfo)