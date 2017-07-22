#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Jul 20, 2017

@author: wlx
'''

import MySQLdb
import time

from UELogSchedule.util.Decorators import retries_on_exception


class MySqlHandler(object):
    '''
    classdocs
    '''

    def __init__(self, mysql_config):
        '''
        Constructor
        '''
        self._dataBaseName = mysql_config['name']
        self._host = mysql_config['ip']
        self._port = mysql_config['port']
        self._userName = mysql_config['user']
        self._password = mysql_config['password']
        self._charset = mysql_config['charset']
        self._mysql_config = mysql_config
        self._repeat = 3
        self._conn = None
        self._init_conn()

    def _init_conn(self):
        self._conn = self._get_conn()
        if self._conn is None:
            raise 'mysql connet fail!'
        self._cursor = self._get_cursor()

    # 获取数据库连接
    def _get_conn(self):
        conn = None
        for i in range(self._repeat):
            try:
                conn = MySQLdb.connect(host=self._host,
                                       user=self._userName,
                                       passwd=self._password,
                                       db=self._dataBaseName,
                                       charset=self._charset)
                if conn:
                    return conn
            except:
                time.sleep(10)
                print i
        return conn

    # 获取cursor
    def _get_cursor(self):
        return self._conn.cursor()

    # 关闭连接
    def _conn_close(self):
        if self._conn is not None:
            self._conn.close()

    # 关闭cursor
    def _cursor_close(self):
        if self._cursor is not None:
            self._cursor.close()

    # 关闭所有
    def close(self):
        self._cursor_close()
        self._conn_close()

    # 创建表
    def create_table(self, data):
        self._cursor.execute(data)
        self._conn.commit()

    def excute_sql(self, sql, params):
        @retries_on_exception(2, hook=self._init_conn)
        def _excute_sql(self, sql, params):
            if self._conn is None:
                self._init_conn()
            try:
                result = self._cursor.execute(sql, params)
                self._conn.commit()
            except:
                self._conn.rollback()
                self.close()
                self._conn = None
                raise
            return result
        return _excute_sql(self, sql, params)

    def insert(self, table, param_dict):
        key_list = []
        value_list = []
        for k, v in param_dict.items():
            key_list.append(k)
            value_list.append(v)
        value_format = ('%s,' * len(value_list)).strip(',')
        sql = 'insert into ' + table + '(' + ','.join(key_list) + ')values(' + value_format + ')'
        return self.excute_sql(sql, value_list)

    # 删除数据
    def delete_data(self, table, condition):
        sql = 'delete from ' + table + ' where ' + condition
        return self.excute_sql(sql, '')

    # 查询数据
    def query(self, sql, params):
        self.excute_sql(sql, params)
        result = self._cursor.fetchall()
        return result

    # 数据库连接信息
    def print_info(self):
        print('数据库连接信息:' + self.dataBaseName + self.host + self.port +
              self.userName + self.password + self.charset)

    # 数据库中表情况
    def show_tables(self):
        sql = 'show tables'
        self.excute_sql(sql, "")
        for row in self._cursor.fetchall():
            print(row)

    # 删除表
    def delete_table(self, table):
        sql = "drop table if exists " + table
        self._cursor.execute(sql)
        self._conn.commit()


if __name__ == '__main__':
    #     tableList = ['temp']
    #     tableName = 'temp'
    #     data = '''
    #         CREATE TABLE IF NOT EXISTS rt_autotest_records(
    #         id int(11) auto_increment NOT NULL primary key,
    #         date date,
    #         testcase_name TEXT,
    #         domain  VARCHAR(255));
    #         '''
    #     expire_time = datetime.date(2013, 05, 21)
    #     insetParams = {'date': '2013-05-21',
    #                    'testcase_name': 'testcasename',
    #                    'domain': u'应用领域' }
    #     mysql = MySqlHandler(MYSQL_DB)
    print "end"
#     mysql.create_table(data)
#     mysql.insert('rt_autotest_records', insetParams)
#     print mysql.show_tables()
#     print mysql.query('select %s from %s where %s=%s', [a,b,c])
