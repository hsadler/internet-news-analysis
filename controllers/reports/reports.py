#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Reports Controller

import pprint
import logging

from models.database.database import MySQL_DB
from models.article.article import Article
from models.headline_word.headline_word import HeadlineWord

from utils.time import get_past_timestamp_by_duration

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/reports.log', level=logging.DEBUG)



class Reports():



    @classmethod
    def send_weekly_report(cls):

        print 'sending weekly report...'

        # db size
        db_size = MySQL_DB.get_size()
        pp.pprint(db_size)

        durations = ['day', 'week', 'month', 'infinite']

        for dur in durations:
            cls.get_report_by_duration(dur)

        # number of articles of last 24 hours
        # number of headline_words last 24 hours
        # top 10 headline words of last 24 hours

        # number of articles of last week
        # number of headline_words of last week
        # top 10 headline words of last week

        # number of articles of last month
        # number of headline_words of last month
        # top 10 headline words of last month

        # total number of articles
        # total number of headline_words
        # top 10 headline words of all time



    @staticmethod
    def get_report_by_duration(duration):

        print 'getting report for duration {0}'.format(duration)













