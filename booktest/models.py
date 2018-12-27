#!/usr/bin/env python
# encoding:utf-8
from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btile = models.CharField(max_length=30)
    bpub_data = models.DateField()