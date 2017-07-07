#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 7, 2017

@author: wlx
'''
from django.conf.urls import url

from UELogApp import views


urlpatterns = [
    url(r'^queryResult/(?P<userId>[0-9]+)/$', views.queryResult),
    url(r'^startParserAndCalc/$', views.startParserAndClac),
]
