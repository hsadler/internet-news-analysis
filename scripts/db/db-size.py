
import MySQLdb as mdb
import pprint

pp = pprint.PrettyPrinter(indent=4)


con = mdb.connect(host='localhost', user='root', passwd='', db='internet_news_analysis')
cur = con.cursor(mdb.cursors.DictCursor)

with con:

    cur.execute(
        """SELECT table_schema "internet_news_analysis",
        SUM(data_length + index_length) / (1024 * 1024) "Database Size in MB"
        FROM information_schema.TABLES GROUP BY table_schema"""
    )

    record = cur.fetchone()

    pp.pprint(record)


