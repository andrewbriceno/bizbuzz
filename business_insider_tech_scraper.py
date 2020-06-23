from bs4 import BeautifulSoup
import requests
import sqlite3

def main():
    req = requests.get("https://www.businessinsider.com/sai")
    soup = BeautifulSoup(req.content, 'lxml')

    #Finds all of the titles and urls of the page's briefings and statements
    urls = []
    titles = []
    summary = []

    for div in soup.find_all("div", class_="tout-text-wrapper default-tout"):
        a_tag = div.find("a")
        summary_tag = div.find("div")
        #print(a_tag.attrs["href"][0])
        if a_tag.attrs["href"][0] == "/":
            urls.append("https://businessinsider.com" + a_tag.attrs["href"])
        else:
            urls.append(a_tag.attrs["href"])
        titles.append(a_tag.text)
        summary.append(summary_tag.text.strip())

    lists = zip(titles, urls)
    # n = 1
    # for x, y, z in zip(titles, urls, summary):
    #     print(str(n) + ". " + x + "\n" + y, sep="\n") #prints each briefings title and its url
    #     print("\n" + z + "\n")
    #     n += 1

    insert(lists)

#FIXME: how to avoid duplicates in the database?
def insert(lists):
    conn = sqlite3.connect('news.db')

    # create database if it doesn't exist yet
    conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
             (TITLE           TEXT,
              URL             TEXT);''')

    #deletes old BI news
    conn.execute('''DELETE FROM NEWS WHERE URL LIKE '%businessinsider.com%';''')

    # insert the title and url of each article in DB
    for title, url in lists:
        conn.execute("INSERT INTO NEWS (TITLE, URL) VALUES (?, ?)",
                     (title, url))
        conn.commit()

    # prints out the content of the DB
    cursor = conn.execute("SELECT TITLE, URL from NEWS")
    for row in cursor:
        print("TITLE = ", row[0])
        print("URL = ", row[1])


if __name__ == '__main__':
    main()