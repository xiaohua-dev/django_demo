from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('ifconfig eth0'.encode("utf-8")).read()
    result = command_status.decode
    return HttpResponse("%s" %(result))
