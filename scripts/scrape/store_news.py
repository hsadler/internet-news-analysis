
# store news items methods

import sys
import MySQLdb as mdb


def store_news_item(
    title,
    scrape_ts,
    url=None,
    author=None,
    description=None,
    publish_ts=None
):
    if(title is None or scrape_ts is None):
        raise ValueError('store_news_item did not receive all necessary data.')
        return None

    con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
    cur = con.cursor()

    with con:

        query = """INSERT INTO news_items(title, scrape_ts, url, author, description, publish_ts)
        VALUES(%s, %s, %s, %s, %s, %s);"""

        cur.execute(query, (title, scrape_ts, url, author, description, publish_ts))





