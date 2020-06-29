from bs4 import BeautifulSoup
import requests

def main():
    #In order: Tech, Finance, Strategy, Retail, Executive, Prime, Intelligence, Politics, Transportation, Markets,
    # Science, News, Media, Enterprise
    BIurls = ["https://www.businessinsider.com/sai", "https://www.businessinsider.com/clusterstock",
              "https://www.businessinsider.com/warroom", "https://www.businessinsider.com/retail",
              "https://www.businessinsider.com/thelife", "https://www.businessinsider.com/prime",
              "https://www.businessinsider.com/research", "https://www.businessinsider.com/politics",
              "https://www.businessinsider.com/transportation", "https://www.businessinsider.com/moneygame",
              "https://www.businessinsider.com/science", "https://www.businessinsider.com/news",
              "https://www.businessinsider.com/media","https://www.businessinsider.com/enterprise"]

    urls = []
    titles = []
    summary = []

    for scrape in BIurls:
        req = requests.get(scrape)
        soup = BeautifulSoup(req.content, 'lxml')

        #Finds all of the titles, urls, and summaries of each article
        for div in soup.find_all("div", class_="top-vertical-trio-item"):
            a_tag = div.find("a", class_="tout-title-link")
            if a_tag.attrs["href"][0] == "/":
                urls.append("https://businessinsider.com" + a_tag.attrs["href"])
            else:
                urls.append(a_tag.attrs["href"])
            titles.append(a_tag.text)
            summary_tag = div.find("div", class_="tout-copy three-column")
            summary.append(summary_tag.text.strip())

        # for div in soup.find_all("div", class_="tout-text-wrapper default-tout"):
        #     a_tag = div.find("a")
        #     if a_tag.attrs["href"][0] == "/":
        #         urls.append("https://businessinsider.com" + a_tag.attrs["href"])
        #     else:
        #         urls.append(a_tag.attrs["href"])
        #     titles.append(a_tag.text)
        #     summary_tag = div.find("div")
        #     summary.append(summary_tag.text.strip())

    n = 1
    for x, y, z in zip(titles,urls, summary):
        print(str(n) + ". " + x + "\n" + y, sep="\n") #prints each article's title, url, and summary/comment
        print(z + "\n")
        n += 1

if __name__ == '__main__':
    main()