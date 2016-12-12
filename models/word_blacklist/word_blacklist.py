#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# HeadlineWord Model

import pprint

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)


class WordBlacklist():


    _blacklist = None
    _cache_is_valid = False


    @classmethod
    def get_blacklist(cls):

        # if cached version of blacklist exists and the cache is valid, return cached word_blacklist
        if cls._blacklist is not None and cls._cache_is_valid:
            print 'retrieving cached version of word_blacklist...'
            return cls._blacklist

        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            print 'retrieving word_blacklist from database...'
            cur.execute('SELECT word FROM word_blacklist WHERE active = 1')
            records = cur.fetchall()

        blacklist = []
        for record in records:
            blacklist.append(record['word'])
        
        cls._blacklist = blacklist
        cls._cache_is_valid = True
        
        return blacklist


    @classmethod
    def add_to_blacklist(cls, word):
        
        # insert word into word_blacklist table
        db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
            try:
                query = 'INSERT INTO word_blacklist(word, active) VALUES("{0}", 1)'.format(word)
                cur.execute(query)
                # invalidate cache
                cls._cache_is_valid = False
            except:
                print 'could not insert word into blacklist: {0}'.format(word)


    @staticmethod
    def remove_from_blacklist(word):
        pass
        # set word as inactive in word_blacklist table
        # invalidate cache

        



