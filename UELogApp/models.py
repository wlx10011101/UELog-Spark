# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from bson.json_util import default

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
    isfPath = models.CharField(max_length=255, default=None)
    hdfsPath = models.CharField(max_length=255, default=None)
    parserStatus = models.CharField(max_length=20, default="NOT_COMPLETE")
    calcStatus = models.CharField(max_length=20, default="NOT_COMPLETE")
    recordTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isfPath
