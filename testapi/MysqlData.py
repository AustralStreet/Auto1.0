#!/usr/bin/env python
# encoding: utf-8

"""
@author: clover
@file: MysqlData.py
@time: 2018/9/4 23:29
"""

import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig


config = configparser.ConfigParser()
config.read(GetTestConfig("dbconfig.conf"))
db='TESTDB'
host = config[db]['host']
user = config[db]['user']
password = config[db]['passwd']
db = config[db]['db']

class MySQLcaozuo():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db,
            charset=config[db]['charset'],
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        """清空数据表"""
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()

    def insert(self, table_name, data):
        """插入数据"""
        for key in data:
            data[key] = "'"+str(data[key])+"'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value +")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def select(self,table_name):
        """查询数据"""
        real_sql = "select * from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            cursor.fetchall()
            self.connection.commit()

    def update(self,table_name):
        """更新数据"""
        real_sql = "update" + table_name + "set votes = 11"+";"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def close(self):
        self.connection.close()

    # if __name__ == ' main ':
    #     db = MySQLData()
    #     table_name = "poll_question"
    #     data = {'id':1, 'question_text':'你喜欢的游戏是什么？'}
    #     db.clear(table_name)
    #     db.insert(table_name, data)
    #     db.close()