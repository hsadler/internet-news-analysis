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


        # filter article_ids to only contain article_ids yet to be processed
        article_ids_for_processing = []

        for article_id in article_ids:

            if HeadlineWord.record_exists_by_article_id(article_id):
                # print 'headline_word records already exist from article id: {0}'.format(article_id)
                pass
            else:
                article_ids_for_processing.append(article_id)


        # batch fetch article models by article_id
        articles = Article.get_by_article_ids(article_ids_for_processing)

        
        # create and save headline_words from articles
        for article in articles:

            headline_words = [w for w in article.title.split() if HeadlineWord.word_is_valid(w)]

            for word in headline_words:

                HeadlineWord.create(
                    word = word,
                    article_id = article.article_id,
                    scrape_ts = article.scrape_ts
                ).save()

            # print 'create_headline_words_from_article success'                    
        


    @classmethod
    def process_all_headlines(cls, batch_amount, force=False):


        print 'process_all_headlines START...'

        
        # if force is true, truncate headline_word table for fresh processing
        if force:
            HeadlineWord.delete_all()

        
        max_id = Article.get_max_article_id()


        # batch process all headlines
        batch_group = 0
        current_batch_start = batch_group * batch_amount + 1
        current_batch_end = current_batch_start + batch_amount

        while current_batch_start <= max_id:

            print 'current_batch_start: {0}'.format(current_batch_start)
            print 'current_batch_end: {0}'.format(current_batch_end - 1)

            batch_range = range(current_batch_start, current_batch_end)

            cls.create_headline_words_from_articles(batch_range)

            batch_group += 1

            current_batch_start = batch_group * batch_amount + 1
            current_batch_end = current_batch_start + batch_amount


        print 'process_all_headlines SUCCESS...'




