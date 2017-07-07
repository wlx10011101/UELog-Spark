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
