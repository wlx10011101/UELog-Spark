#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 8, 2017

@author: wlx
'''
import time
from UELogApp.models import ResultRecord


starQcatMissionResetful = ""
queryQcatMissionResetful = ""
startSparkMissionResetful = ""
querySparkMissionResetful = ""


'''
@input: appName, sparkServer, configXml, hdfs
@hdfs: hdfs://10.9.171.160:9000/user/wlx/test1/sample_03-14.13-58.json
@sparkMissionKEY: hdfs:__10.9.171.160:9000_user_wlx_test1_sample_03-14.13-58.json
@qcatMissionRESULE: hdfs://10.9.171.160:9000/user/wlx/test1/sample_03-14.13-58_result.json
'''

'''
@input: Log  Hdfs
@LogFilePath: D:\\UELOG_ISF\\sample_03-14.13-58.isf
@remoteHdfsPath: //user//wlx//test1 ?
@qcatMissionKEY: D:_UELOG_ISF_sample_03-14.13-58.isf
@qcatMissionRESULE: D:\\UELOG_ISF\\sample_03-14.13-58.json
'''

HDFS_ROOT_PATH = "http://10.9.171.160:9000"


class LogMissionController(object):
    '''
    classdocs
    '''

    def __init__(self, isfFile, hdfsPath):
        '''
        Constructor
        '''
        self._isfFile = isfFile
        self._hdfsRelativePath = hdfsPath

    def startQcatMission(self):
        inputData = {"Log": self._isfFile, }
        # make input data for qcatresetful, and start

    def queryQcatMission(self):
        # save last status of mission ,when status channged ,save to db
        # return True when the status of mission is success, and return False when misssion status is Fail
        pass

    def startSparkMission(self):
        pass

    def querySparkMission(self):
        pass

    def start(self):
        pass
