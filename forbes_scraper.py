from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sqlite3

def main():
    req = requests.get('https://www.forbes.com/business')
    soup = BeautifulSoup(req.content, features='html.parser')

    urls = []
    titles = []
    summary = []

    #finds each article
    articles=soup.findAll('h2')

    for article in articles:
        if article.a is not None:
            url = (article.a['href'])
            urls.append(url)
            req = requests.get(url)
            soup = BeautifulSoup(req.content, features='html.parser')
            titles.append(soup.find('title').text)
            first_para = soup.find('div', class_="article-body-container")
            first_line = first_para.find('p').text
            summary.append(first_line)

    title_url_map=zip(titles, urls, summary)

    #for elem in lists:
        #print(elem)

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