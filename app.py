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
def process_article_headline(article_id):
	ArticleProcessor.create_headline_words_from_article(article_id)




# testing headline words
from models.headline_word.headline_word import HeadlineWord

def create_headline_word_and_save():
	HeadlineWord().create('hi', 1, 1234).save().print_dict()


# testing article retrieval
from models.article.article import Article

def get_article_by_id(article_id):
    Article.get_by_article_id(article_id).print_dict()
