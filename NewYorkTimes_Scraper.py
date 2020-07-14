from bs4 import BeautifulSoup
import requests

def main():
    #Technology, Business, Economy, Energy, Science, Space
    NYTurls = ["https://www.nytimes.com/section/technology", "https://www.nytimes.com/section/business",
               "https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/energy-environment",
               "https://www.nytimes.com/section/science", "https://www.nytimes.com/section/science/space"]

    urls = set()
    titles = set()
    summaries = set()

    for scrape in NYTurls:
        req = requests.get(scrape)
        soup = BeautifulSoup(req.content, 'lxml')

        for div in soup.find_all("li", class_="css-ye6x8s"):
            a_tag = div.find("a")
            if a_tag.attrs["href"][0] == "/":
                urls.add("https://nytimes.com" + a_tag.attrs["href"])
            else:
                urls.add(a_tag.attrs["href"])
            titles.add(a_tag.find("h2").text)
            summaries.add(a_tag.find("p").text)

    # n = 1
    # for x, y, z in zip(titles, urls, summaries):
    #     print(str(n) + ". " + x + "\n" + y, sep="\n")  # prints each article's title, url, and summary/comment
    #     print("\n" + z + "\n")
    #     n += 1

if __name__ == '__main__':
    main()