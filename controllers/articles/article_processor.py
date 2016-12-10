#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Article Processing Controller

import pprint
import logging

from models.article.article import Article
from models.headline_word.headline_word import HeadlineWord

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/scrape.log', level=logging.DEBUG)



class ArticleProcessor():


    @staticmethod
    def create_headline_words_from_article(article_id):

        # check if words have been created from article_id already
        if HeadlineWord.record_exists_by_article_id(article_id):
            print 'headline_word records already exist from article id: {0}'.format(article_id)
            return False

        # TODO: improve word validation and stripping
        def word_is_valid(word):
            return len(word) > 1

        article = Article.get_by_article_id(article_id)

        headline_words = [w for w in article.title.split() if word_is_valid(w)]

        for word in headline_words:

            HeadlineWord.create(
                word = word,
                article_id = article.article_id,
                scrape_ts = article.scrape_ts
            ).save()

        print 'create_headline_words_from_article success'


    @classmethod
    def create_headline_words_from_articles(cls, article_id_list):
        
        for article_id in article_id_list:
            cls.create_headline_words_from_article(article_id)


    @staticmethod
    def process_all_headlines():
        print 'im next...'















