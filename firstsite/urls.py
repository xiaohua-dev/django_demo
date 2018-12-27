from django.contrib import admin
from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', view.hello),
]
