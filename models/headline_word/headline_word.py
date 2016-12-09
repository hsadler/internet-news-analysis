#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# HeadlineWord model

import pprint

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)


class HeadlineWord():


    def __init__(self, word, article_id, sc):
        
        self.id = None
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
            self.id = cur.fetchone()['LAST_INSERT_ID()']

        return self


    def print_dict(self):
        output = {
            'id': self.id,
            'word': self.word,
            'article_id': self.article_id,
            'scrape_ts': self.scrape_ts
        }
        pp.pprint(output)




