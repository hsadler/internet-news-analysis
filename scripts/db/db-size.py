#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import pprint

pp = pprint.PrettyPrinter(indent=4)


con = mdb.connect(host='localhost', user='root', passwd='', db='internet_news_analysis')
cur = con.cursor(mdb.cursors.DictCursor)

with con:

    cur.execute("""
        SELECT table_name AS "Table",
        ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
        FROM information_schema.TABLES
        WHERE table_schema = "internet_news_analysis"
        ORDER BY (data_length + index_length) DESC;
    """)

    record = cur.fetchone()

    pp.pprint(record)


