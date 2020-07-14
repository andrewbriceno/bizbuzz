from bs4 import BeautifulSoup
import requests

def main():
    #Tech, Science, Business, Features
    TTurls = ["https://www.techtimes.com/personaltech", "https://www.techtimes.com/science",
              "https://www.techtimes.com/biztech", "https://www.techtimes.com/feature"]

    urls = set()
    titles = set()
    summaries = set()

    for scrape in TTurls:
        req = requests.get(scrape)
        soup = BeautifulSoup(req.content, 'lxml')

        for div in soup.find_all("div", class_="list2"):
            #gets url and title
            a_tag = div.find("h2").find("a")
            urls.add(a_tag.attrs["href"])
            titles.add(a_tag.text)
            #gets summary
            p_tag = div.find("p", class_="summary")
            summaries.add(p_tag.text)

    # n = 1
    # for x, y, z in zip(titles, urls, summaries):
    #     print(str(n) + ". " + x + "\n" + y, sep="\n")  # prints each article's title, url, and summary/comment
    #     print("\n" + z + "\n")
    #     n += 1

if __name__ == '__main__':
    main()