#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''


class Reflection:

    @staticmethod
    def create_obj(packetName, className, *args):
        module = __import__(packetName, globals(), locals(), [className])
        obj = getattr(module, className)
        return obj(*args)

    @staticmethod
    def invoke(obj, methodName, *args):
        method = getattr(obj, methodName)
        return method(*args)
