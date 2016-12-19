#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Testing



from models.email.email import Email

# Email('harrysadlermusic@gmail.com', 'my subject', 'hi there').send().print_dict()



from controllers.reports.reports import Reports

Reports.send_weekly_report()


from models.headline_word.headline_word import HeadlineWord

# HeadlineWord.get_top_headline_words_count_by_timestamp_period(1481609486, 1481609586, 20)
