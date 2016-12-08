#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Scrape controller

import requests
import pprint
import time
import logging
from xml.etree import ElementTree

from models.user_agent.user_agent import UserAgent
from models.article.article import Article

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/scrape.log', level=logging.DEBUG)


class Scrape():



    @staticmethod
    def google_news_scrape():


        log_text = 'google rss scrape started: {0}'.format(time.ctime())
        print log_text
        logging.info(log_text)


        scrape_url = 'https://news.google.com/news?output=rss'

        scrape_headers = {
            'User-Agent': UserAgent.get_random()
        }


        res = requests.get(scrape_url, headers=scrape_headers)

        tree = ElementTree.fromstring(res.content)
        items = tree.find('channel').findall('item')


        for item in items:

            url = item.find('link').text
            title = item.find('title').text
            pub_time = item.find('pubDate').text

            article = Article()
            article.create(url=url, title=title)
            article.save()


        log_text = 'google rss scrape ended: {0}'.format(time.ctime())
        print log_text
        logging.info(log_text)




    @staticmethod
    def newsapi_scrape():


        log_text = 'newsapi json scrape started: {0}'.format(time.ctime())
        print log_text
        logging.info(log_text)


        news_api = {
            'get_sources_url': 'https://newsapi.org/v1/sources?language=en',
            'get_articles_url': 'https://newsapi.org/v1/articles',
            'api_key': '9110ce6d759d455392a0d83606bf59db'
        }


        sources_headers = {
            'User-Agent': UserAgent.get_random()
        }

        sources_res = requests.get(news_api['get_sources_url'], headers=sources_headers)
        sources_data = sources_res.json()['sources']


        source_ids = []

        for sources_item in sources_data:
            source_id = sources_item[u'id']
            source_ids.append(source_id)


        for s_id in source_ids:

            time.sleep(5)

            get_url = '{0}?source={1}&apiKey={2}'.format(
                news_api['get_articles_url'],
                s_id,
                news_api['api_key']
            )

            articles_headers = {
                'User-Agent': UserAgent.get_random()
            }

            articles_res = requests.get(get_url, headers=articles_headers)
            articles_data = articles_res.json()


            for article_dict in articles_data[u'articles']:

                article = Article()
                article.create(
                    title=article_dict[u'title'],
                    url=article_dict[u'url'],
                    author=article_dict[u'author'],
                    description=article_dict[u'description']
                )
                article.save()


        log_text = 'newsapi json scrape ended: {0}\n'.format(time.ctime())
        print log_text
        logging.info(log_text)



