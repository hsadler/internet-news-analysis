
import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)


scrape_url = 'https://news.google.com/news?output=rss'


print('scraping {0}...'.format(scrape_url))
