#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Database Connection model

import MySQLdb as mdb



class MySQL_DB():



    def __init__(self):

        self.connection = mdb.connect(host='localhost', user='root', passwd='', db='internet_news_analysis')
        self.cur = self.connection.cursor(mdb.cursors.DictCursor)

        self.connection.set_character_set('utf8')
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')



    @classmethod
    def get_size(cls):

        db = cls()

        with db.connection:
            db.cur.execute("""
                SELECT table_name AS "Table",
                ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
                FROM information_schema.TABLES
                WHERE table_schema = "internet_news_analysis"
                ORDER BY (data_length + index_length) DESC;
            """)

            return db.cur.fetchall()




