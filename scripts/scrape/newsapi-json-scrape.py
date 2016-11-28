
import requests
import pprint
import time

from user_agent import get_rand_user_agent as rand_user_agent
from article_model import Article


pp = pprint.PrettyPrinter(indent=4)


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

    # u'author': u'http://www.abc.net.au/news/zoe-daniel/166858',
    # u'description': u"Conservative senator Cory Bernardi warns the Liberal Party not to ignore the lessons of Donald Trump's victory in the US presidential election.",
    # u'publishedAt': u'2016-11-28T05:15:45Z',
    # u'title': u'Bernardi warns Liberals must learn lessons from Trump victory',
    # u'url': u'http://www.abc.net.au/news/2016-11-28/bernardi-warns-liberals-must-learn-lessons-trump-victory/8062738',
    # u'urlToImage': u'http://www.abc.net.au/news/image/7403226-1x1-700x700.jpg'
    #
    # self.title = title
    # self.url = url
    # self.author = author
    # self.description = description
    # self.publish_ts = publish_ts

    for article_dict in articles_data[u'articles']:

        article = Article()
        article.create(
            title=article_dict[u'title'],
            url=article_dict[u'url'],
            author=article_dict[u'author'],
            description=article_dict[u'description']
        )
        article.save()

        # pp.pprint(article_dict)


















