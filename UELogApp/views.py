# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import threading

from UELogApp.MissionSchedule import Controller
from UELogApp.models import ResultRecord

THREAD_NUM = 1
# Create your views here.


@csrf_exempt
def queryResult(request, userId):
    return HttpResponse(serializers.serialize('json', ResultRecord.objects.filter(userId=userId)))


@csrf_exempt
def startParserAndClac(request):
    if request.method != "POST":
        return HttpResponse(status=403, reason="start Parser and calculate only use POST")
    data = json.loads(request.body)
    '''
    注: request.body为list,so,in this list, only have qcatFilePath that need parser and calc
    '''
    print data, type(data)
    if THREAD_NUM:
        threading.Thread(target=Controller(data).start).start()
        THREAD_NUM -= 1
    return HttpResponse("post reviced")