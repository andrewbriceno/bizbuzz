from bs4 import BeautifulSoup
import requests

def main():
    MWurls = ["https://www.marketwatch.com/"]

    urls = set()
    titles = set()
    summaries = set()

    for scrape in MWurls:
        req = requests.get(scrape)
        soup = BeautifulSoup(req.content, 'lxml')
        #Finds all of the titles, urls, and summaries of each article
        for div in soup.find_all("div", class_="article__content"):
            h3 = div.h3
            if h3 is not None:
                a_tag = h3.find("a", class_="link")
                if a_tag is not None and "Opinion:" not in a_tag.text:
                    url = a_tag.attrs["href"]
                    try:
                        req = requests.get(url)
                    except Exception:
                        continue
                    urls.add(url)
                    title = a_tag.text.strip()
                    titles.add(title)
                    soup = BeautifulSoup(req.content, 'lxml')
                    sum = soup.find('p').text.replace('\n', ' ')
                    summaries.add(sum)
                    print(a_tag.text.strip())
                    print(a_tag.attrs["href"])
                    print(sum.replace('\n', ' '))


if __name__ == '__main__':
    main()