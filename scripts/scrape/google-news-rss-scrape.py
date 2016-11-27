
import requests
import pprint
import time

from xml.etree import ElementTree
from user_agent import get_rand_user_agent as rand_user_agent
from article_model import Article


pp = pprint.PrettyPrinter(indent=4)


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
    article.print_dict()


