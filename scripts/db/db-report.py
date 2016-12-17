#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import pprint


pp = pprint.PrettyPrinter(indent=4)


con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
cur = con.cursor(mdb.cursors.DictCursor)


with con:


    print '\n=====================================================\n'


    # count articles table records
    cur.execute("""
        SELECT count(*) AS count FROM articles;
    """)

    articles_count = cur.fetchone()['count']

    print 'articles count: {0}'.format(articles_count)


    # count headline_words table records
    cur.execute("""
        SELECT count(*) AS count FROM headline_words;
    """)

    headline_words_count = cur.fetchone()['count']

    print 'headline words count: {0}'.format(headline_words_count)


    # get top ten occuring headline words
    cur.execute("""
        SELECT word, count(*) AS count FROM headline_words GROUP BY word ORDER BY count(*) DESC LIMIT 10;
    """)

    top_ten_words = cur.fetchall()
    words = []
    for word_item in top_ten_words:
        words.append('{0}: {1}'.format(word_item['word'], word_item['count']))

    print '\ntop 10 words:\n\n{0}'.format('\n'.join(words))


    print '\n=====================================================\n'




