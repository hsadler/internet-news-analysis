
import requests
import pprint

from user_agent import get_rand_user_agent as rand_user_agent
from xml.etree import ElementTree


pp = pprint.PrettyPrinter(indent=4)


scrape_url = 'https://news.google.com/news?output=rss'

scrape_headers = {
    'User-Agent': rand_user_agent()
}

res = requests.get(scrape_url, headers=scrape_headers)
tree = ElementTree.fromstring(res.content)

items = tree.find('channel').findall('item')

pp.pprint(items)