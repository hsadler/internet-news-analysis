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



    def __init__(self, title, article_id=None, url=None, author=None,
        description=None, publish_ts=None, scrape_ts=None, md5hash=None):

        self.title = title
        self.article_id = article_id
        self.url = url
        self.author = author
        self.description = description
        self.publish_ts = publish_ts
        self.scrape_ts = scrape_ts
        self.md5hash = md5hash



    # create instance from gathered data
    @classmethod
    def create(cls, title, url=None, author=None, description=None, publish_ts=None):

        return cls(
            title = title,
            url = url,
            author = author,
            description = description,
            publish_ts = publish_ts,
            scrape_ts = int(time.time()),
            md5hash = hashlib.md5(title.encode('ascii', 'ignore')).hexdigest()
        )



    # create instance from db record
    @classmethod
    def create_from_db_record(cls, record):

        return cls(
            title = record['title'],
            article_id = record['id'],
            url = record['url'],
            author = record['author'],
            description = record['description'],
            publish_ts = record['publish_ts'],
            scrape_ts = record['scrape_ts'],
            md5hash = record['md5hash']
        )



    # retrieve article record from db and create instance
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

        return cls.create_from_db_record(record)



    # save model to db record
    def save(self):

        article_exists_in_db = self.record_exists_by_md5hash(self.md5hash)
        if article_exists_in_db:
            return False

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:

            query = """
                INSERT INTO articles(title, url, author, description, publish_ts,
                scrape_ts, md5hash) VALUES(%s, %s, %s, %s, %s, %s, %s);
            """

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



    # check if article exists in db by article hash
    def record_exists_by_md5hash(self, md5hash):

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            cur.execute("SELECT * FROM articles WHERE md5hash = '{0}'".format(md5hash))
            record = cur.fetchone()

        return record is not None



    def print_dict(self):
        pp.pprint(self.__dict__)




