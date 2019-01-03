#!/usr/bin/env python
# encoding:utf-8
from django.http import HttpResponse
import os

def hello(request):
    command_status = os.popen('ifconfig eth0').read()
    return HttpResponse("%s" %(command_status))
