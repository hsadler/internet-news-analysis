#!/usr/local/bin/python

import requests
import pprint
import time
import logging

from user_agent import get_rand_user_agent as rand_user_agent
from article_model import Article


pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='scrape.log', level=logging.INFO)


logging.info('newsapi scrape started: {0}'.format(time.ctime()))


news_api = {
    'get_sources_url': 'https://newsapi.org/v1/sources?language=en',
    'get_articles_url': 'https://newsapi.org/v1/articles',
    'api_key': '9110ce6d759d455392a0d83606bf59db'
}


sources_headers = {
    'User-Agent': rand_user_agent()
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
        'User-Agent': rand_user_agent()
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


logging.info('newsapi scrape ended: {0}\n'.format(time.ctime()))

















