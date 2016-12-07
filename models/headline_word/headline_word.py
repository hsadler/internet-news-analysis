#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# HeadlineWord model

import pprint

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)


class HeadlineWord():


    def __init__(self):
        self.word = None
        self.article_id = None
        self.scrape_ts = None


    def create(self, word, article_id, scrape_ts):

        self.word = word
        self.article_id = article_id
        self.scrape_ts = scrape_ts

        return True


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

        return True


    def print_dict(self):
        output = {
            'word': self.word,
            'article_id': self.article_id,
            'scrape_ts': self.scrape_ts
        }
        pp.pprint(output)




