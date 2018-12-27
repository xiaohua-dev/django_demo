#!/usr/bin/env python
# encoding:utf-8
from django.db import models

# Create your models here.

#一类
class BookInfo(models.Model):
    btile = models.CharField(max_length=30)
    bpub_data = models.DateField()


#多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hgender = models.CharField(max_length=248)
    hbook = models.ForeignKey('BookInfo')#两表之间建立关系