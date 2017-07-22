#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''
import logging
import os
import time

from UELogSchedule.Config import UELOG_MYSQL_DB, RESULT_TABLE, RESULT_TABLE_NAME, HDFS_USER_PATH
from UELogSchedule.DataBase.MySql import MySqlHandler
from UELogSchedule.util.Singleton import Singleton


ISOTIMEFORMAT = '%Y-%m-%d %X'
NOT_COMPLETE = 0
SUCCESS = 1
FAIL = -1
ALL_KEY = ['IsfFilePath', 'HdfsResultPath', 'ParserStatus', 'CalcStatus', 'RecordTime']


@Singleton
class ResultRecordDb(object):
    '''
    classdocs
    '''

    def __init__(self):
        self._mysqlHandle = MySqlHandler(UELOG_MYSQL_DB)
        self._init_table()

    def _init_table(self):
        self._mysqlHandle.create_table(RESULT_TABLE % RESULT_TABLE_NAME)

    def insert(self, paramDict):
        self._mysqlHandle.insert(RESULT_TABLE_NAME, paramDict)

    def query(self, isfFilePath, queryKey=ALL_KEY):
        key = ','.join(queryKey)
        queryDatas = self._mysqlHandle.query('SELECT {1} FROM `{0}` WHERE IsfFilePath=%s'.format(RESULT_TABLE_NAME, key), [isfFilePath])
        result = []
        for data in queryDatas:
            dataDict = dict(zip(queryKey, data))
            if 'RecordTime' in dataDict:
                dataDict['RecordTime'] = dataDict['RecordTime'].strftime(ISOTIMEFORMAT)
            result.append(dataDict)
        return result

    def query_success_record(self, queryKey=ALL_KEY):
        key = ','.join(queryKey)
        queryDatas = self._mysqlHandle.query('SELECT {1} FROM `{0}` WHERE ParserStatus=1 AND CalcStatus=1'.format(RESULT_TABLE_NAME, key), [])
        result = []
        for data in queryDatas:
            dataDict = dict(zip(queryKey, data))
            if 'RecordTime' in dataDict:
                dataDict['RecordTime'] = dataDict['RecordTime'].strftime(ISOTIMEFORMAT)
            result.append(dataDict)
        return result

    def query_over_record(self, queryKey=ALL_KEY):
        key = ','.join(queryKey)
        queryDatas = self._mysqlHandle.query('SELECT {1} FROM `{0}` WHERE ParserStatus!=0 AND CalcStatus!=0'.format(RESULT_TABLE_NAME, key), [])
        result = []
        for data in queryDatas:
            dataDict = dict(zip(queryKey, data))
            if 'RecordTime' in dataDict:
                dataDict['RecordTime'] = dataDict['RecordTime'].strftime(ISOTIMEFORMAT)
            result.append(dataDict)
        return result

    def new_add_record(self, isfFilePath):
        if not self.query(isfFilePath):
            hdfsFilePath = HDFS_USER_PATH + os.path.split(isfFilePath.replace('\\', '/'))[1].replace('.isf', '_result.json')
            now = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            paramDict = {'IsfFilePath': isfFilePath,
                         'HdfsResultPath': hdfsFilePath,
                         'ParserStatus': None,
                         'CalcStatus': None,
                         'RecordTime': now
                         }
            self.insert(paramDict)
            return True
        else:
            logging.error('{} The same record exists!'.format(isfFilePath))
            return False

    def update_parser_status(self, status, isfFilePath):
        self._mysqlHandle.excute_sql('update {0} set ParserStatus=%s where IsfFilePath=%s'.format(RESULT_TABLE_NAME), [status, isfFilePath])
        return True

    def update_calc_status(self, status, isfFilePath):
        self._mysqlHandle.excute_sql('update {0} set CalcStatus=%s where IsfFilePath=%s'.format(RESULT_TABLE_NAME), [status, isfFilePath])

    def start_parser(self, isfFilePath):
        self.update_parser_status(NOT_COMPLETE, isfFilePath)
        return True

    def success_parser(self, isfFilePath):
        self.update_parser_status(SUCCESS, isfFilePath)
        return True

    def faile_parser(self, isfFilePath):
        self.update_parser_status(FAIL, isfFilePath)
        self.update_calc_status(FAIL, isfFilePath)
        return True

    def start_calc(self, isfFilePath):
        self.update_calc_status(NOT_COMPLETE, isfFilePath)
        return True

    def success_calc(self, isfFilePath):
        self.update_calc_status(SUCCESS, isfFilePath)
        return True

    def fail_calc(self, isfFilePath):
        self.update_calc_status(FAIL, isfFilePath)
        return True

if __name__ == "__main__":
    isfFile = 'D:\\UELOG_ISF\\sample_03-14.13-59_.isf'

    rd = ResultRecordDb()
#     rd.new_add_record(isfFile)
#     rd.success_parser(isfFile)
#     rd.success_calc(isfFile)
    print rd.query_over_record()
