#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Reports Controller

import pprint
import time

from models.database.database import MySQL_DB
from models.article.article import Article
from models.headline_word.headline_word import HeadlineWord
from models.email.email import Email

from utils.time_utils import get_past_timestamp_by_duration
from utils.time_utils import get_human_readable_from_timestamp

pp = pprint.PrettyPrinter(indent=4)



class Reports():



    @classmethod
    def send_report(cls):


        report_parts = []


        report_parts.append(
            '\nReport: {0}\n\n=====================================================\n\n'.format(
                get_human_readable_from_timestamp(time.time())
            )
        )


        # db size
        db_size = MySQL_DB.get_size()

        for line in db_size:
            report_parts.append(
                'Table: {0}\nSize: {1} MB\n'.format(
                    line['Table'], line['Size (MB)']
                )
            )



        report_parts.append(
            '-----------------------------------------------------\n'
        )


        durations = ['day', 'week', 'month', 'all time']

        for dur in durations:
            dur_report = cls.get_report_by_duration(dur)
            report_parts.extend([dur_report, '\n'])


        report_parts.append(
            '=====================================================\n'
        )


        recipient = 'harrysadlermusic@gmail.com'
        subject = 'Internet News Analysis Report {0}'.format(
            get_human_readable_from_timestamp(time.time())
        )
        body = '\n'.join(report_parts)

        Email(recipient, subject, body).send()



    @staticmethod
    def get_report_by_duration(duration):


        start = get_past_timestamp_by_duration(duration)
        end = int(time.time())


        article_count = Article.get_count_by_timestamp_period(start, end)
        headline_word_count = HeadlineWord.get_count_by_timestamp_period(start, end)

        counts = '{0}\narticle count: {1}\nheadline word count: {2}\n'.format(
            duration.upper(),
            article_count,
            headline_word_count
        )


        ranked_headline_words = HeadlineWord.get_top_ranked_words_by_timestamp_period(start, end)

        ranked = []

        for ranked_word in ranked_headline_words:

            ranked_word_str = '{0}: {1}'.format(ranked_word['word'], ranked_word['count'])
            ranked.append(ranked_word_str)


        return '\n'.join([counts, '\n'.join(ranked)])








