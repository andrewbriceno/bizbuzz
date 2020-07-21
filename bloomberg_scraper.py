from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

def main():

    hdr = {'User-Agent': 'Mozilla/5.0', "accept-language": "en-US"}

    BBurls = ["https://www.bloomberg.com/markets","https://www.bloomberg.com/markets",
              "https://www.bloomberg.com/technology", "https://www.bloomberg.com/pursuits",
              "https://www.bloomberg.com/sooner-than-you-think", "https://www.bloomberg.com/businessweek",
              "https://www.bloomberg.com/deals",]

    urls = set()
    titles = set()
    summaries = set()

    for scrape in BBurls:
        req = Request(scrape, headers=hdr)
        response = urlopen(req, timeout=10)
        page_content = response.read().decode('utf-8')
        soup = BeautifulSoup(page_content, 'lxml')

        #Headline articles
        for a in soup.find_all("a", class_="single-story-module__headline-link"):
            title = a.text.strip()
            titles.add(title)
            url = "bloomberg.com"+a.attrs["href"]
            urls.add(url)
            #req = Request(scrape, headers=hdr)
            #response = urlopen(req, timeout=10)
            #page_content = response.read().decode('utf-8')
            #soup = BeautifulSoup(page_content, 'lxml')
            #if soup.find('meta') is not None and soup.find('meta').content is not None:
            #    sum = soup.find('meta').content
            #    summaries.add(sum)
            #else:
            sum = "No summary available. Click on the card to view the full article."
            summaries.add(sum)
            #print(title)
            #print(url)
            #print(sum)

        #'Related-story' articles
        for div in soup.find_all("div", class_="single-story-module__related-story mod-related-story"):
            a_tag = div.a
            if a_tag is not None:
                title = a_tag.text.strip()
                titles.add(title)
                url = "bloomberg.com" + a_tag.attrs["href"]
                urls.add(url)
                #req = Request(scrape, headers=hdr)
                #response = urlopen(req, timeout=10)
                #page_content = response.read().decode('utf-8')
                #soup = BeautifulSoup(page_content, 'lxml')
                #if soup.find('meta') is not None and soup.find('meta').content is not None:
                #    sum = soup.find('meta').content
                #    summaries.add(sum)
                #else:
                sum = "No summary available. Click on the card to view the full article."
                summaries.add(sum)
                #print(title)
                #print(url)
                #print(sum)

        #All other articles
        for h3 in soup.find_all("h3", class_="story-package-module__story__headline"):
            a_tag = h3.a
            if a_tag is not None:
                title = a_tag.text.strip()
                titles.add(title)
                url = "bloomberg.com" + a_tag.attrs["href"]
                urls.add(url)
                #req = Request(scrape, headers=hdr)
                #response = urlopen(req, timeout=10)
                #page_content = response.read().decode('utf-8')
                #soup = BeautifulSoup(page_content, 'lxml')
                #if soup.find('meta') is not None and soup.find('meta').content is not None:
                    #sum = soup.find('meta').content
                    #summaries.add(sum)
                #else:
                sum = "No summary available. Click on the card to view the full article."
                summaries.add(sum)
                #print(title)
                #print(url)
                #print(sum)

    for x, y, z in zip(titles, urls, summaries):
        print(x)
        print(y)
        print(z)

if __name__ == '__main__':
    main()