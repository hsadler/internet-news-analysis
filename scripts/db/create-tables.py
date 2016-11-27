
import MySQLdb as mdb


con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
cur = con.cursor()

with con:

    # create news_items table
    cur.execute("""CREATE TABLE IF NOT EXISTS news_items(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        url VARCHAR(1000),
        author VARCHAR(100),
        title VARCHAR(255) NOT NULL,
        description VARCHAR(255),
        scrape_ts INT(12) NOT NULL,
        publish_ts INT(12)
    );""")

