#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Main App

from controllers.scrape.scrape import Scrape
from controllers.articles.article_processor import ArticleProcessor



# scrapers
def google_news_scrape():
    Scrape.google_news_scrape()

def newsapi_scrape():
    Scrape.newsapi_scrape()



# article processing
def process_article_headlines(article_ids):
	ArticleProcessor.create_headline_words_from_articles(article_ids)

def process_all_headlines(batch_amount=20, force=False):
	ArticleProcessor.process_all_headlines(batch_amount, force)



# word blacklist
from models.word_blacklist.word_blacklist import WordBlacklist

def add_blacklist_word(words):
	WordBlacklist.add_to_blacklist(words)






