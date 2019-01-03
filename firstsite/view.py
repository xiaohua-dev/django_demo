from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('cat /space/aa.txt').read()
    return HttpResponse("%s".decode() %(command_status))
