from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.
# 定义视图函数，httprequest
# 2、进行url配置，建立url地址和视图的对应关系
#http://127.0.0.1:8000/index

def index(request):
    #进行处理，和M和T进行交互
    #return HttpResponse("booktest app")

    # 如何使用模板文件
    # 1.加载模板文件，模板对象
    temp = loader.get_template('booktest/index.html')
    # 2、定义模板上下文：给模板文件传递数据；以字典的方式
    context = RequestContext(request, {})

    # 3、模板渲染：产生标准的html内容
    res_html = render(context, temp)
    # 4、返回给浏览器
    return HttpResponse(res_html)


def index2(request):
    return HttpResponse("hello world")