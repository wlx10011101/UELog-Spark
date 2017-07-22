#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''
import os
import re
import requests

from UELogSchedule.Config import HDFS_USER_PATH
from UELogSchedule.Service.Resetful import QCAT_MISSIONS, QCAT_QUERY_MISSIONS,\
    SPARK_MISSIONS, SPARK_QUERY_MISSIONS
from UELogSchedule.DataBase.ResultRecord import ResultRecordDb


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


def startQcatMission():
    while QCAT_MISSIONS.not_empty:
        item = QCAT_MISSIONS.get()
        inputData = {"Log": item[0], "Hdfs": HDFS_USER_PATH}
        response = requests.post(url=starQcatMissionResetful, json=inputData)
        ResultRecordDb().new_add_record(item[0])
        if re.match('.*Error.*', response.text):
            ResultRecordDb().faile_parser(item[0])
        else:
            ResultRecordDb().start_parser(item[0])
            QCAT_QUERY_MISSIONS.put(item[0])


def queryQcatMission():
    while QCAT_QUERY_MISSIONS.not_empty:
        item = QCAT_QUERY_MISSIONS.get()
        result = requests.get(url=queryQcatMissionResetful + item.replace('\\', '_')).text
        if re.match(".*Error.*", result) or result == "FAIL":
            ResultRecordDb().faile_parser(item)
        elif result == "SUCCESS":
            ResultRecordDb().success_parser(item)
            SPARK_MISSIONS.put(item)
        else:
            QCAT_QUERY_MISSIONS.put(item)


def startSparkMission():
    sparkServer = 'spark://10.9.171.160:7077'
    configXml = None
    HDFS_BASE_PATH = HDFS_ROOT_PATH.replace('http', 'hdfs') + HDFS_USER_PATH

    inputData = {
        "appName": None,
        "soarkServer": sparkServer,
        "configXml": None or configXml,
        "hdfs": None
    }
    while SPARK_MISSIONS.not_empty:
        item = SPARK_MISSIONS.get()
        hdfsFileName = os.path.split(item.replace('\\', '/'))[1].replace('.isf', '.json')
        hdfsFilePath = HDFS_BASE_PATH + hdfsFileName
        missionKey = hdfsFileName.replace('/', '_')
        inputData["appName"] = hdfsFileName
        inputData['hdfs'] = hdfsFilePath
        result = requests.post(url=startSparkMissionResetful, json=inputData).text
        if re.match('.*Error.*', result):
            ResultRecordDb().fail_calc(item)
        else:
            ResultRecordDb().success_calc(item)
            SPARK_QUERY_MISSIONS.put((item, missionKey))


def querySparkMission():
    while SPARK_QUERY_MISSIONS.not_empty:
        item = SPARK_QUERY_MISSIONS.get()
        result = requests.get(url=querySparkMissionResetful + item[1]).text
        if re.match(".*Error.*", result) or result == "FAIL":
            ResultRecordDb().fail_calc(item[0])
        elif result == "SUCCESS":
            ResultRecordDb().success_calc(item[0])
        else:
            SPARK_QUERY_MISSIONS.put(item)
