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



# testing article retrieval
from models.article.article import Article

def get_articles_by_ids(article_ids):
    articles = Article.get_by_article_ids(article_ids)
    for article in articles:
    	article.print_dict()
