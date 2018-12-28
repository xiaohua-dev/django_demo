from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#定义视图函数，httprequest
#http://127.0.0.1:8000/index

def index(request):
    return HttpResponse("booktest app")