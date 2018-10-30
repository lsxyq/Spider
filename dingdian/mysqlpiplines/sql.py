#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

import pymysql
MYSQL_HOSTS ='127.0.0.1'
MYSQL_USER='root'
MYSQL_PASSWORD='root'
MYSQL_PORT = 3306
MYSQL_DB = 'xiaoshuo'


conn = pymysql.connect(
    host=MYSQL_HOSTS,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD,
    db=MYSQL_DB,
    charset="utf8")
# 获取游标对象
cursor = conn.cursor()


class Sql():
    @classmethod
    def insert_dd_name(cls,xs_name,xs_author,category,name_id):
        sql = '''INSERT INTO dd_name(xs_name,xs_author,category,name_id) VALUES (%s,%s,%s,%s)'''
        values = (xs_name,xs_author,category,name_id)
        cursor.execute(sql,values)
        conn.commit()
    @classmethod
    def select_name(cls,name_id):
        sql='''select count(*) from dd_name where name_id=%s'''
        cursor.execute(sql,(name_id,))
        return cursor.fetchall()[0]