#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''

import logging
import time


def CalcTime(func):
    def _deco(*args, **kwargs):
        now = time.time()
        result = func(*args, **kwargs)
        elapsedTime = time.time() - now
        print "method: {0} Time running:{1}".format(func.func_name, time.strftime('%H:%M:%s:%S', time.localtime(elapsedTime)))
        return result
    return _deco


def TryAgain(func):
    def _deco(*args, **kwargs):
        maxTime = 3
        while(maxTime):
            try:
                return func(*args, **kwargs)
            except Exception:
                maxTime = maxTime - 1
                print "Try {0} Time Failed".format(3 - maxTime)
    return _deco


def retries_on_exception(maxTries, hook=None, hookArg=None, hookGrainSize=1,
                         exceptions=(Exception,)):
    def dec(func):
        def f2(*args, **kwargs):
            hookGrainSizeInit = hookGrainSize
            tries = range(maxTries)
            tries.reverse()
            for triesRemaining in tries:
                hookGrainSizeInit = hookGrainSizeInit - 1
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if triesRemaining > 0:
                        if hookGrainSizeInit == 0:
                            hookGrainSizeInit = hookGrainSize
                            if hook is not None:
                                if hookArg is not None:
                                    hook(hookArg)
                                else:
                                    hook()
                    else:
                        logging.error('try ' + str(maxTries) + ' times, but excute ' + func.__name__ + ' is still fail')
                        raise
                else:
                    break
        return f2
    return dec

if __name__ == "__main__":
    @TryAgain
    def printa(a):
        a.c()
    printa('c')
