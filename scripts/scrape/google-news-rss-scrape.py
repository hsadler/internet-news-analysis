
import requests
import pprint
import time

from xml.etree import ElementTree
from user_agent import get_rand_user_agent as rand_user_agent
from store_news import store_news_item


pp = pprint.PrettyPrinter(indent=4)


scrape_url = 'https://news.google.com/news?output=rss'

scrape_headers = {
    'User-Agent': rand_user_agent()
}


res = requests.get(scrape_url, headers=scrape_headers)

tree = ElementTree.fromstring(res.content)
items = tree.find('channel').findall('item')


for item in items:

    article = {}
    article['url'] = item.find('link').text
    article['title'] = item.find('title').text
    article['publish_time'] = item.find('pubDate').text

    store_news_item(
        url=article['url'],
        title=article['title'],
        scrape_ts=int(time.time())
    )


