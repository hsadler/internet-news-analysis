#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scripts.scrape.google_news_scrape import scrape as g_scrape
from scripts.scrape.newsapi_scrape import scrape as n_scrape


# scrapers
def google_news_scrape():
    g_scrape()

def newsapi_scrape():
    n_scrape()


