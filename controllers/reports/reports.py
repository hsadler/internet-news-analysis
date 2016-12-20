#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Reports Controller

import pprint
import time

from models.database.database import MySQL_DB
from models.article.article import Article
from models.headline_word.headline_word import HeadlineWord

from utils.time_utils import get_past_timestamp_by_duration

pp = pprint.PrettyPrinter(indent=4)



class Reports():



    @classmethod
    def send_weekly_report(cls):


        # print 'sending weekly report...'

        report_parts = []


        # db size
        db_size = MySQL_DB.get_size()
        for line in db_size:
            print line
            report_parts.append(line)


        durations = ['day', 'week', 'month', 'infinite']

        for dur in durations:
            dur_report = cls.get_report_by_duration(dur)
            print dur_report
            report_parts.append(dur_report)

        # print '\n'.join(report_parts)

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

        start = get_past_timestamp_by_duration(duration)
        end = int(time.time())

        # article count
        article_count = Article.get_count_by_timestamp_period(start, end)

        print '{0} articles for duration {1} to {2}'.format(article_count, start, end)

        # word count
        # top ten words

        # return 'past: {0} and present: {1}'.format(past, present)























