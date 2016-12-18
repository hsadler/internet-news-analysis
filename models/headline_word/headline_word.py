#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# HeadlineWord Model

import pprint

from models.database.database import MySQL_DB
from models.word_blacklist.word_blacklist import WordBlacklist

pp = pprint.PrettyPrinter(indent=4)



class HeadlineWord():



    def __init__(self, word, article_id, scrape_ts, word_id=None):

        self.word_id = word_id
        self.word = word
        self.article_id = article_id
        self.scrape_ts = scrape_ts



    @classmethod
    def create(cls, word, article_id, scrape_ts):

        return cls(
            word = word,
            article_id = article_id,
            scrape_ts = scrape_ts
        )



    def save(self):

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:

            query = """
                INSERT INTO headline_words(word, article_id, scrape_ts) VALUES(%s, %s, %s);
            """

            data = (
                self.word,
                self.article_id,
                self.scrape_ts,
            )

            cur.execute(query, data)

            cur.execute('SELECT LAST_INSERT_ID();')
            self.word_id = cur.fetchone()['LAST_INSERT_ID()']

        return self



    @staticmethod
    def word_is_valid(word):

        return len(word) > 1 and word.lower() not in WordBlacklist.get_blacklist()



    @staticmethod
    def record_exists_by_article_id(article_id):

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            query = 'SELECT * FROM headline_words WHERE article_id = {0}'.format(article_id)
            cur.execute(query)
            record = cur.fetchone()

        return record is not None



    @staticmethod
    def get_top_headline_words_count_by_timestamp_period(start_ts, end_ts, word_amount=10):

        print 'getting top {0} headline words from {1} to {2}'.format(
            word_amount,
            start_ts,
            end_ts
        )



    @staticmethod
    def delete_all():

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            cur.execute('TRUNCATE TABLE headline_words')

        print 'table headline_words truncated...'



    def print_dict(self):
        pp.pprint(self.__dict__)


