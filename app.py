#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from controllers.scrape.scrape import Scrape
from controllers.articles.article_processor import ArticleProcessor



# scrapers
def google_news_scrape():
    Scrape.google_news_scrape()

def newsapi_scrape():
    Scrape.newsapi_scrape()



# article processing
def test_process_article():
	ArticleProcessor.create_headline_words_from_article(1)



#testing
from models.headline_word.headline_word import HeadlineWord

def test():
	HeadlineWord().create('hi', 1, 1234).save().print_dict()
