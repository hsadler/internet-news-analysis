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


    @staticmethod
    def process_all_headlines():
        print 'im next...'















