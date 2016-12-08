#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from controllers.scrape.scrape import Scrape


# scrapers
def google_news_scrape():
    Scrape.google_news_scrape()

def newsapi_scrape():
    Scrape.newsapi_scrape()


#testing
from models.headline_word.headline_word import HeadlineWord

def test():
	HeadlineWord().create('hi', 1, 1234).save().print_dict()
