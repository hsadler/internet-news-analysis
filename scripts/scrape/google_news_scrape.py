#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import pprint
import time
import logging
from xml.etree import ElementTree

from scripts.scrape.user_agent import get_rand_user_agent as rand_user_agent
from models.article.article import Article


pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(filename='logs/scrape.log', level=logging.DEBUG)



def scrape():


    log_text = 'google rss scrape started: {0}'.format(time.ctime())
    print log_text
    logging.info(log_text)


    scrape_url = 'https://news.google.com/news?output=rss'

    scrape_headers = {
        'User-Agent': rand_user_agent()
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




