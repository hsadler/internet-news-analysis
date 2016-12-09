#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Article Model

import sys
import time
import hashlib
import pprint

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)



class Article():


    def __init__(self, article_id=None, title, url=None, author=None, description=None, publish_ts=None):
        
        self.article_id = article_id
        self.title = title
        self.url = url
        self.author = author
        self.description = description
        self.publish_ts = publish_ts

        self.scrape_ts = int(time.time())
        self.md5hash = hashlib.md5(title.encode('ascii', 'ignore')).hexdigest()


    @classmethod
    def create(cls, title, url=None, author=None, description=None, publish_ts=None):

        return cls(
            title = title,
            url = url,
            author = author,
            description = description,
            publish_ts = publish_ts         
        )


    @classmethod
    def get_by_article_id(cls, article_id):
        
        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:

            query = 'SELECT * FROM articles WHERE id = {0}'.format(article_id)
            cur.execute(query)
            record = cur.fetchone()

        if record is None:
            return False

        # TODO: STOPPED HERE!!!!!!!!!





    def save(self):

        article_exists_in_db = self.exists_by_md5hash(self.md5hash)
        if article_exists_in_db:
            return False

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:

            query = """INSERT INTO articles(title, url, author, description,
            publish_ts, scrape_ts, md5hash) VALUES(%s, %s, %s, %s, %s, %s, %s);"""

            data = (
                self.title,
                self.url,
                self.author,
                self.description,
                self.publish_ts,
                self.scrape_ts,
                self.md5hash
            )

            cur.execute(query, data)

            cur.execute('SELECT LAST_INSERT_ID();')
            self.article_id = cur.fetchone()['LAST_INSERT_ID()']

        return self


    def exists_by_md5hash(self, md5hash):

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            cur.execute("SELECT * FROM articles WHERE md5hash = '{0}'".format(md5hash))
            record = cur.fetchone()

        return record is not None


    def print_dict(self):
        pp.pprint(self.__dict__)




