from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('cat /space/aa.txt').read()
    aa = command_status.encode("utf-8")
    return HttpResponse("%s".decode() %(aa))
