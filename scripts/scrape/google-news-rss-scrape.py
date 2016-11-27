
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

for item in items:
	# url, title, publish time, (description, maybe)
	article = {}
	article['url'] = item.find('link').text
	article['title'] = item.find('title').text
	article['publish_time'] = item.find('pubDate').text

	for prop in article:
		print '{0}: {1}'.format(prop, article[prop])

