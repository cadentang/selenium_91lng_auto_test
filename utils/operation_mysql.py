# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:对MySQL数据库相关操作
"""

import pymysql, xlwt, time


class MyDB:

    def __init__(self, database_type):
        # 测试环境
        self.host = "#",
        self.port = "3306",
        self.username = "root",
        self.password = "#",
        self.bpm_database = "test_91lng_bpm",
        self.tms_database = "test_91lng_tms",
        self.consumer_database = "test_91lng_consumer",
        self.database_type = ["bpm", "tms", "consumer"]

        # 数据库连接配置
        if database_type == self.database_type[0]:
            self.db = self.bpm_database
        elif database_type == self.database_type[1]:
            self.db = self.tms_database
        else:
            self.db = self.consumer_database

        self.config = {
            'host': str(self.host),
            'user': self.username,
            'password': self.password,
            'port': int(self.port),
            'db': self.db
        }

        self.db_connect = None
        self.cursor = None

    def connectDB(self):
        """
        连接数据库
        """
        try:
            self.db_connect = pymysql.connect(**self.config)
            # 创建游标
            self.cursor = self.db_connect.cursor()
            print("数据库连接成功!")
        except ConnectionError as ex:
            print(str(ex))

    def executeSQL(self, sql_):
        """
        执行sql
        """
        self.connectDB()
        self.cursor.execute(sql_)
        value = self.cursor.fetchall()
        self.db_connect.commit()
        return value

    def get_all(self, cursor):
        """
        得到所有执行sql后的结果
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        得到一条sql语句执行结果
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        关闭数据库连接
        :return:
        """
        self.db_connect.close()
        print("关闭数据库成功！")

    def export(self, sql_):
        # 查询的结果导出到Excel中
        results = self.executeSQL(sql_)
        self.cursor.scroll(0, mode='absolute')
        filename = '123.xls'  # 定义Excel名字

        # 获取MYSQL里面的数据字段名称
        fields = self.cursor.description
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('table', cell_overwrite_ok=True)

        # 在Excel中写入MySQL列字段信息
        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])

        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])
        workbook.save(filename)