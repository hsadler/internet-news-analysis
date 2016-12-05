
import MySQLdb as mdb


con = mdb.connect('localhost', 'root', '', 'internet_news_analysis')
cur = con.cursor()

with con:

    cur.execute('DROP TABLE articles;')
    cur.execute('DROP TABLE headline_keywords;')

    # create articles table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS articles(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        url VARCHAR(1000),
        author VARCHAR(255),
        title VARCHAR(1000) NOT NULL,
        description VARCHAR(1000),
        scrape_ts INT(12) NOT NULL,
        publish_ts INT(12),
        md5hash VARCHAR(32));
    """)

    # create headline_keywords table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS headline_keywords(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        keyword VARCHAR(50) NOT NULL,
        article_id INT(8) NOT NULL,
        scrape_ts INT(12) NOT NULL);
    """)
