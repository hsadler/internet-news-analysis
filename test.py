#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Testing



# empty db and do a fresh article scrape
from controllers.scrape.scrape import Scrape

Scrape.google_news_scrape()



# from controllers.reports.reports import Reports

# Reports.send_report()


# from utils.time_utils import get_month_timestamp_from_timestamp

# get_month_timestamp_from_timestamp(1482736371)
