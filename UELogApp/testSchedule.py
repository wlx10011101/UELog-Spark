#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 8, 2017

@author: wlx
'''
import threading

from UELogApp.MissionSchedule import Controller


if __name__ == '__main__':
    data = ["file1.json"]
    threading.Thread(target=Controller(data).startQcatMission).start()