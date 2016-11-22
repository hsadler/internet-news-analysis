
import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)


news_api = {
    'get_sources_url': 'https://newsapi.org/v1/sources?language=en',
    'get_articles_url': 'https://newsapi.org/v1/articles',
    'api_key': '9110ce6d759d455392a0d83606bf59db'
}

sources_res = requests.get(news_api['get_sources_url'])
sources_data = sources_res.json()['sources']


source_ids = []

for sources_item in sources_data:
    source_id = sources_item[u'id']
    source_ids.append(source_id)


for s_id in source_ids:
    print('making source id api calls...')



