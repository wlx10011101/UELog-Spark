#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''
from time import strftime

from UELogSchedule.DataBase.MySql import MySqlHandler


UELOG_MYSQL_DB = {
    "ip": "10.9.178.141",
    "port": "3306",
    "name": "UELog-Server",
    "user": "root",
    "password": "",
    "charset": "utf8"
}

RESULT_TABLE = '''
    CREATE TABLE IF NOT EXISTS %s
    (
        id int(11) auto_increment NOT NULL primary key,
        IsfFilePath       VARCHAR(255),
        HdfsResultPath    VARCHAR(255),
        ParserStatus      TINYINT,
        CalcStatus        TINYINT,
        RecordTime        DATETIME
    );
    '''
RESULT_TABLE_NAME = 'result_records'


HDFS_ROOT_HTTP = "http://10.9.171.160:9000"
# QCAT_SERVER_HOST = "http://10.9.171.160:23456"
# SPARK_SERVER_HOST = "http://10.9.171.160:34567"
# starQcatMissionResetful = QCAT_SERVER_HOST + "/parserByqcat"
# queryQcatMissionResetful = QCAT_SERVER_HOST + "/QueryParserResult/"
# startSparkMissionResetful = SPARK_SERVER_HOST + "/calcByspark"
# querySparkMissionResetful = SPARK_SERVER_HOST + "/QueryCalcResult/"

HDFS_USER_PATH = '/user/wlx/test1/'
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
