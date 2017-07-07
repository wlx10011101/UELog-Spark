# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from UELogApp.models import ResultRecord


# Create your views here.
@csrf_exempt
def queryResult(request, userId):
    return HttpResponse(serializers.serialize('json', ResultRecord.objects.filter(userId=userId)))


@csrf_exempt
def startParserAndClac(request):
    if request.method != "POST":
        return HttpResponse(status=403, reason="start Parser and calculate only use POST")

    print request.body[1:]
    return HttpResponse("post reviced")
