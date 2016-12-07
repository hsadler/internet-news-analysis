#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scripts.scrape.google_news_scrape import scrape as g_scrape
from scripts.scrape.newsapi_scrape import scrape as n_scrape


# scrapers
def google_news_scrape():
    g_scrape()

def newsapi_scrape():
    n_scrape()


#testing
from models.headline_word.headline_word import HeadlineWord

def test():
	HeadlineWord().create('hi', 1, 1234).save().print_dict()
