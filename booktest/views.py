from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo

# Create your views here.
# 定义视图函数，httprequest
# 2、进行url配置，建立url地址和视图的对应关系
#http://127.0.0.1:8000/index

def index(request):
    #进行处理，和M和T进行交互
    #return HttpResponse("booktest app")

    # # 如何使用模板文件
    # # 1.加载模板文件，模板对象
    # temp = loader.get_template('booktest/index.html')
    #
    # # 2、定义模板上下文：给模板文件传递数据；以字典的方式
    # context = RequestContext(request, {})
    #
    # # 3、模板渲染：产生标准的html内容
    # res_html = temp.render(context)
    #
    # # 4、返回给浏览器
    # return HttpResponse(res_html)

    # 以上四步实际上就是调用render的函数，等于下方式
    return render(request, 'booktest/index.html', {'content': 'hello xiaopeng', 'list': list(range(1,10))})

def index2(request):
    return HttpResponse("hello world")



def show_books(request):
    """显示图书的信息"""
    # 1、通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2、使用模板
    return render(request,'booktest/show_books.html', {'books': books})

def detail(request, bid):
    """查询图书关联英雄信息"""
    # 1、根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)

    # 2、查询和book关联的英雄信息
    heros = book.heroinfo_set.all()

    return render(request,'booktest/detail.html', {'book': book, 'heros': heros})