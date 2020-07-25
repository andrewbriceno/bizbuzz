from bs4 import BeautifulSoup
import requests

def main():
    req = requests.get("https://www.forbes.com/enterprise-tech")
    soup = BeautifulSoup(req.content, 'lxml')
    for div in soup.find_all("div", class_="stream-item__text"):
        a_tag = div.a
        if a_tag is not None:
            url = a_tag.attrs["href"]
            title = a_tag.text
            sum = div.find("div",class_="stream-item__description").text

if __name__ == '__main__':
    main()