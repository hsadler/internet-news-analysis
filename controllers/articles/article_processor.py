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
    def create_headline_words_from_articles(article_ids):
        
        
        # TODO: improve word validation and stripping
        def word_is_valid(word):
            return len(word) > 1


        # filter article_ids to only contain article_ids yet to be processed
        article_ids_for_processing = []

        for article_id in article_ids:

            if HeadlineWord.record_exists_by_article_id(article_id):
                print 'headline_word records already exist from article id: {0}'.format(article_id)
            else:
                article_ids_for_processing.append(article_id)


        # batch fetch article models by article_id
        articles = Article.get_by_article_ids(article_ids_for_processing)

        
        # create and save headline_words from articles
        for article in articles:

            headline_words = [w for w in article.title.split() if word_is_valid(w)]

            for word in headline_words:

                HeadlineWord.create(
                    word = word,
                    article_id = article.article_id,
                    scrape_ts = article.scrape_ts
                ).save()

            print 'create_headline_words_from_article success'                    
        


    @staticmethod
    def process_all_headlines(batch_amount, force):

        print 'in prog...'

        # get max article_id from articles table

        # batch process all headlines in groups of 20





