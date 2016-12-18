#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Reports Controller

import pprint
import logging

from models.article.article import Article
from models.headline_word.headline_word import HeadlineWord

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/reports.log', level=logging.DEBUG)



class Reports():


    @staticmethod
    def send_weekly_report():
        print 'sending weekly report...'

        # db size

        # number of articles
        # number of headline_words

        # top 10 headline words of last 24 hours

        # top 10 headline words of last week

        # top 10 headline words of last month

        # top 10 headline words of all time




