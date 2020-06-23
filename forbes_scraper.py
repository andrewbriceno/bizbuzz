from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import sqlite3

def main():
    myurl = 'https://www.forbes.com/business'

    # open up connection and grab the page
    uclient = urlopen(myurl)
    page_html = uclient.read()
    uclient.close()

    #parse the page for h2 tags
    page_soup = soup(page_html, 'html.parser')
    article_titles = page_soup.findAll('h2')

    #maps each article title to its URL
    title_url_map = {}
    for title in article_titles:
        if title.a is not None:
            title_url_map[title.a.find(text=True)]=title.a['href']

    #print the map
    # for article in title_url_map:
    #     print("Title:", article, "\nURL:",title_url_map[article])

    # method for inserting title and URL into database, just comment out if not needed
    insert(title_url_map)

#FIXME: how to avoid duplicates in database
def insert(title_url_map):
    conn = sqlite3.connect('news.db')

    # create database if it doesn't exist yet
    conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
             (TITLE           TEXT,
              URL             TEXT);''')

    #deletes old Forbes news
    conn.execute('''DELETE FROM NEWS WHERE URL LIKE '%www.forbes.com%';''')

    # insert the title and url of each article in DB
    for article in title_url_map:
        article = str(article)
        url = str(title_url_map[article])
        conn.execute("INSERT INTO NEWS (TITLE, URL) VALUES (?, ?)",
                     (article, url))
        conn.commit()

    # prints out the content of the DB
    cursor = conn.execute("SELECT TITLE, URL from NEWS")
    for row in cursor:
        print("TITLE = ", row[0])
        print("URL = ", row[1])


if __name__ == '__main__':
    main()