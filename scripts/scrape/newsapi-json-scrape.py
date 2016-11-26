
import requests
import pprint
import time

from user_agent import get_rand_user_agent as rand_user_agent


pp = pprint.PrettyPrinter(indent=4)


news_api = {
    'get_sources_url': 'https://newsapi.org/v1/sources?language=en',
    'get_articles_url': 'https://newsapi.org/v1/articles',
    'api_key': '9110ce6d759d455392a0d83606bf59db'
}

sources_headers = {
    'User-Agent': rand_user_agent()
}
print sources_headers
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

    articles_res = requests.get(get_url)
    articles_data = articles_res.json()

    print('================================================')

    pp.pprint(articles_data)



