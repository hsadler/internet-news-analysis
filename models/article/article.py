#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Article model

import sys
import time
import hashlib
import pprint

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)


class Article():


    def __init__(self):
        self.title = None
        self.url = None
        self.author = None
        self.description = None
        self.publish_ts = None
        self.scrape_ts = None
        self.md5hash = None


    def create(self, title, url=None, author=None, description=None, publish_ts=None):

        self.title = title
        self.url = url
        self.author = author
        self.description = description
        self.publish_ts = publish_ts

        self.scrape_ts = int(time.time())
        self.md5hash = hashlib.md5(title.encode('ascii', 'ignore')).hexdigest()

        return True


    def save(self):

        article_exists_in_db = self.get_by_md5hash(self.md5hash)
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

        return True


    def get_by_md5hash(self, md5hash):

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            cur.execute("SELECT * FROM articles WHERE md5hash = '{0}'".format(md5hash))
            record = cur.fetchone()

        if record is not None:
            self.title = record['title']
            self.url = record['url']
            self.author = record['author']
            self.description = record['description']
            self.publish_ts = record['publish_ts']
            self.scrape_ts = record['scrape_ts']
            self.md5hash = record['md5hash']

        return record is not None


    def print_dict(self):
        output = {
            'title': self.title,
            'url': self.url,
            'author': self.author,
            'description': self.description,
            'publish_ts': self.publish_ts,
            'scrape_ts': self.scrape_ts,
            'md5hash': self.md5hash
        }
        pp.pprint(output)




