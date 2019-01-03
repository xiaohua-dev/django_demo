from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('cat /space/aa.txt').read()
    return HttpResponse("%s".encode("utf-8") %(command_status))
