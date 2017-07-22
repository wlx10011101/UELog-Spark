#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 18, 2017

@author: wlx
'''
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return HttpResponse('''
            Here is backend of UELogServer''')
