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

    # finds each article
    articles = soup.findAll('h2')

    for article in articles:
        if article.a is not None:
            url = (article.a['href'])
            req = requests.get(url)
            soup = BeautifulSoup(req.content, features='html.parser')
            first_para = soup.find('div', class_="article-body-container")
            if first_para is None:
                continue
            first_line = first_para.find('p').text
            titles.append(soup.find('title').text)
            urls.append(url)
            summary.append(first_line)

    title_url_map = zip(titles, urls, summary)
    for x, y, z in title_url_map:
        print(x)
        print(y)
        print(z)
        print()
    # myurl = 'https://www.forbes.com/business'
    #
    # # open up connection and grab the page
    # uclient = urlopen(myurl)
    # page_html = uclient.read()
    # uclient.close()
    #
    # #parse the page for h2 tags
    # page_soup = soup(page_html, 'html.parser')
    # article_titles = page_soup.findAll('h2')
    #
    # #Grabs date from Forbes and calculates expiration date
    # for div in page_soup.find_all("div", class_="stream-item__date"):
    #     if div.has_attr('data-date'):
    #         unix_timestamp = int(div['data-date']) / 1000
    #         date = datetime.fromtimestamp(unix_timestamp)  #local timezone
    #         print(date.strftime("%Y-%m-%d %H:%M:%S"))
    #         expiration_date = date + timedelta(days=7)
    #         print(expiration_date.strftime("%Y-%m-%d %H:%M:%S"))
    #
    #
    # #maps each article title to its URL
    # title_url_map = {}
    # for title in article_titles:
    #     if title.a is not None:
    #         title_url_map[title.a.find(text=True)]=title.a['href']

    #print the map
    # for article in title_url_map:
    #     print("Title:", article, "\nURL:",title_url_map[article])

    # method for inserting title and URL into database, just comment out if not needed
    #insert(title_url_map)

#FIXME: how to avoid duplicates in database
# def insert(title_url_map):
#     conn = sqlite3.connect('news.db')
#
#     # create database if it doesn't exist yet
#     conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
#              (TITLE           TEXT,
#               URL             TEXT);''')
#
#     #deletes old Forbes news
#     conn.execute('''DELETE FROM NEWS WHERE URL LIKE '%www.forbes.com%';''')
#
#     # insert the title and url of each article in DB
#     for article in title_url_map:
#         article = str(article)
#         url = str(title_url_map[article])
#         conn.execute("INSERT INTO NEWS (TITLE, URL) VALUES (?, ?)",
#                      (article, url))
#         conn.commit()
#
#     # prints out the content of the DB
#     cursor = conn.execute("SELECT TITLE, URL from NEWS")
#     for row in cursor:
#         print("TITLE = ", row[0])
#         print("URL = ", row[1])


if __name__ == '__main__':
    main()