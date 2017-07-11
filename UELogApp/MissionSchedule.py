#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 8, 2017

@author: wlx
'''
import os
import re
import requests
import time

from UELogApp.models import ResultRecord


HDFS_ROOT_PATH = "http://10.9.171.160:9000"
QCAT_SERVER_HOST = "http://10.9.171.160:23456"
SPARK_SERVER_HOST = "http://10.9.171.160:34567"
starQcatMissionResetful = QCAT_SERVER_HOST + "/parserByqcat"
queryQcatMissionResetful = QCAT_SERVER_HOST + "/QueryParserResult/"
startSparkMissionResetful = SPARK_SERVER_HOST + "/calcByspark"
querySparkMissionResetful = SPARK_SERVER_HOST + "/QueryCalcResult/"


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


class Controller(object):
    '''
    classdocs
    '''

    def __init__(self, isfFile, hdfsPath):
        '''
        Constructor
        '''
        self._isfFile = isfFile
        self._qcatMissionKey = self._isfFile.replace('\\', '_')
        self._hdfsRelativePath = hdfsPath
        self._hdfsAbsolutePath = HDFS_ROOT_PATH.replace('http', 'hdfs') + \
            self._hdfsRelativePath + \
            os.path.split(self._isfFile.replace('\\', '/'))[1].replace('.isf', '.json')
        self._sparkMissionKey = self._hdfsAbsolutePath.replace('/', '_')
#         self._userName = inputUserName
        self._dbRecord = ResultRecord.objects.filter(isfFile=self._isfFile)

    def startQcatMission(self):
        inputData = {"Log": self._isfFile, "Hdfs": self._hdfsRelativePath}
        response = requests.post(url=starQcatMissionResetful, json=inputData)
        return False if re.match('.*Error.*', response.text) else True

    def queryQcatMission(self):
        response = requests.get(url=queryQcatMissionResetful + self._qcatMissionKey)
        return response.text

    def startSparkMission(self):
        sparkServer = 'spark://10.9.171.160:7077'
        configXml = None
        inputData = {
            "appName": None or self._userName,
            "soarkServer": None or sparkServer,
            "configXml": None or configXml,
            "hdfs": self._hdfsAbsolutePath,
        }
        response = requests.post(url=startSparkMissionResetful, json=inputData)
        return False if re.match('.*Error.*', response.text) else True

    def querySparkMission(self):
        response = requests.get(url=querySparkMissionResetful + self._sparkMissionKey)
        return response.text

    def query(self, method):
        queryResult = "NOT_COMPLETE"
        while queryResult == "NOT_COMPLETE":
            queryResult = method()
            time.sleep(300)
        return queryResult

    def match(self, result):
        if re.match(".*Error.*", result) or result == "FAIL":
            return False
        else:
            return True

    def start(self):
        if self.startQcatMission():
            queryResult = self.query(self.queryQcatMission())
            if not self.match(queryResult):
                self._dbRecord.update(parserStatus="FAIL", calcStatus="FAIL")
            else:
                self._dbRecord.update(parserStatus="SUCCESS")
                if self.startSparkMission():
                    queryResult = self.query(self.querySparkMission())
                    if not self.match(queryResult):
                        self._dbRecord.update(calcStatus="FAIL")
                    else:
                        self._dbRecord.update(calcStatus="SUCCESS")
                else:
                    self._dbRecord.update(calcStatus="FAIL")
        else:
            self._dbRecord.update(parserStatus="FAIL", calcStatus="FAIL")
if __name__ == "__main__":
    testData = {
        "Log": "file2.isf",
        "Hdfs": "/user/wlx/test1"
    }
    Controller("D:\UELOG_ISF\sample_03-14.13-58.isf", "/user/wlx/test1/")
