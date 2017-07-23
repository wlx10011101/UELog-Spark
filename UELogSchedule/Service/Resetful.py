#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''
import Queue
from bottle import Bottle, request, run
import json
import logging
import os
import sys
sys.path.append(os.path.abspath("%s/../../" % sys.path[0]))
from UELogSchedule.DataBase.ResultRecord import ResultRecordDb


UELogScheduleApp = Bottle()
QCAT_MISSIONS = Queue.Queue()
SPARK_MISSIONS = Queue.Queue()
QCAT_QUERY_MISSIONS = Queue.Queue()
SPARK_QUERY_MISSIONS = Queue.Queue()


@UELogScheduleApp.route('/startMission', 'post')
def start_mission():
    isfFilePath = request.json.get('IsfFilePath', None)
    hdfsPath = request.json.get('HdfsPath', None)
    if isfFilePath:
        QCAT_MISSIONS.put((isfFilePath, hdfsPath))
        return 'True'
    else:
        return 'False'


@UELogScheduleApp.route('/querySuccessRecord', 'get')
def query_success_record():
    result = ResultRecordDb().query_success_record()
    logging.debug(result)
    return json.dumps(result)


@UELogScheduleApp.route('/queryOverRecord', 'get')
def query_over_record():
    result = ResultRecordDb().query_over_record()
    logging.debug(result)
    return json.dumps(result)


@UELogScheduleApp.route('/queryStatus', 'post')
def query_status():
    isfFilePath = request.json.get('IsfFilePath', None)
    if not isfFilePath:
        result = ResultRecordDb().query(isfFilePath)
        logging.debug(result)
        return json.dumps(result)

if __name__ == "__main__":
    run(app=UELogScheduleApp, host='0.0.0.0', port=4567, debug=logging.DEBUG)
