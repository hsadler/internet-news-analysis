#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import pprint


pp = pprint.PrettyPrinter(indent=4)


con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
cur = con.cursor(mdb.cursors.DictCursor)

with con:

    # create articles table
    cur.execute("""
        SELECT * FROM articles;
    """)

    articles = cur.fetchall()
    pp.pprint(articles)
    print 'article count: {0}'.format(len(articles))

