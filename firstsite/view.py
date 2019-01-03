from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('cat /space/aa.txt'.encode("utf-8")).read()
    return HttpResponse("%s".decode() %(command_status))
