#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''


def Singleton(cls):

    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
