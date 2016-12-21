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

        with db.connection:

            query = """
                INSERT INTO headline_words(word, article_id, scrape_ts) VALUES(%s, %s, %s);
            """

            data = (
                self.word,
                self.article_id,
                self.scrape_ts,
            )

            db.cur.execute(query, data)

            db.cur.execute('SELECT LAST_INSERT_ID();')
            self.word_id = db.cur.fetchone()['LAST_INSERT_ID()']

        return self



    @staticmethod
    def word_is_valid(word):

        return len(word) > 1 and word.lower() not in WordBlacklist.get_blacklist()



    @staticmethod
    def record_exists_by_article_id(article_id):

        db = MySQL_DB()

        with db.connection:
            query = 'SELECT * FROM headline_words WHERE article_id = {0}'.format(article_id)
            db.cur.execute(query)
            record = db.cur.fetchone()

        return record is not None



    @staticmethod
    def get_count_by_timestamp_period(start_ts, end_ts):

        db = MySQL_DB()

        with db.connection:

            query = """
                SELECT count(*) AS count FROM headline_words
                WHERE scrape_ts BETWEEN {0} AND {1};
            """.format(start_ts, end_ts)

            db.cur.execute(query)

            count = db.cur.fetchone()['count']

        return count



    @staticmethod
    def get_top_ranked_words_by_timestamp_period(start_ts, end_ts, word_amount=10):

        print 'getting top {0} headline words from timestamp {1} to timestamp {2}'.format(
            word_amount,
            start_ts,
            end_ts
        )

        db = MySQL_DB()

        with db.connection:

            query = """
                SELECT word, count(*) AS count FROM headline_words
                WHERE scrape_ts BETWEEN {0} AND {1}
                GROUP BY word ORDER BY count(*) DESC LIMIT {2};
            """.format(start_ts, end_ts, word_amount)

            db.cur.execute(query)

            records = db.cur.fetchall()
            pp.pprint(records)

            return records



    @staticmethod
    def delete_all():

        db = MySQL_DB()

        with db.connection:
            db.cur.execute('TRUNCATE TABLE headline_words')

        print 'table headline_words truncated...'



    def print_dict(self):
        pp.pprint(self.__dict__)


