# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Resource(models.Model):
    ftpPath = models.CharField(max_length=255)
    hdfsPath = models.CharField(max_length=255)
    configXml = models.CharField(max_length=255, default=None)
    userId = models.ForeignKey(User)

    def __str__(self):
        return self.hdfsPath


class ResultRecord(models.Model):
    userId = models.ForeignKey(User)
    isfPath = models.FilePathField(path='/home/wlx/Pictures', recursive=True)
    hdfsPath = models.FilePathField(path='/home/wlx/Pictures', recursive=True)
    parserStatus = models.CharField(max_length=20, default="NOT_COMPLETE")
    calcStatus = models.CharField(max_length=20, default="NOT_COMPLETE")
    recordTime = models.DateTimeField(default=None)

    def __str__(self):
        return self.isfPath
