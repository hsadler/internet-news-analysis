#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Article Processing Controller

import pprint
import logging

from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/scrape.log', level=logging.DEBUG)



class ArticleProcessor():


    @staticmethod
    def create_headline_words_from_article(article_id):

    	db = MySQL_DB()
        con = db.connection
        cur = db.cur

        with con:
        	print 'processing article with id: {0}...'.format(article_id)



