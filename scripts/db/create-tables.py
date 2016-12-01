
import MySQLdb as mdb


con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
cur = con.cursor()

with con:

    # cur.execute('DROP TABLE news_items;')

    # create news_items table
    cur.execute("""CREATE TABLE IF NOT EXISTS news_items(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        url VARCHAR(1000),
        author VARCHAR(255),
        title VARCHAR(1000) NOT NULL,
        description VARCHAR(1000),
        scrape_ts INT(12) NOT NULL,
        publish_ts INT(12),
        md5hash VARCHAR(32)
    );""")

