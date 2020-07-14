from bs4 import BeautifulSoup
import requests
import string

def main():
    req = requests.get('https://www.forbes.com/business')
    soup = BeautifulSoup(req.content, features='html.parser')

    punctuations = '''!()-[]{};:\'\"\\”“’’‘‘,<>./?@#$%^&*_~'''

    urls = []
    titles = []
    summary = []
    companies = []
    # for getting which company(s) the article is talking about
    company_master_list = ['AMAZON', 'SAMSUNG', 'IBM', 'TWITTER', 'NETFLIX', 'ORACLE', 'SAP', 'SALESFORCE', 'TESLA', 'MICROSOFT', 'APPLE', 'GOOGLE', 'FACEBOOK']

    # finds each article
    articles = soup.findAll('h2')

    translator = str.maketrans(punctuations, ' ' * len(punctuations))  # map punctuation to space

    for article in articles:
        if article.a is not None:
            # print(article)
            url = (article.a['href'])
            req = requests.get(url)
            soup = BeautifulSoup(req.content, features='html.parser')
            first_para = soup.find('div', class_="article-body-container")
            if first_para is None:
                continue
            sum = first_para.find('p').text
            title = soup.find('title').text
            new_title = title.translate(translator)
            company_check = set(company_master_list).intersection(new_title.upper().split(' '))
            # print(company_check)
            if company_check:
                print(company_check)
                # article = News(title=title, url=url, summary=sum, company=company_check)
                # article.save()
            # title_set = set(soup.find('title').text.upper().split(' '))
            # print(title_set)
            # if companies.intersection(title_set):
            #     print(companies.intersection(title_set))
            # titles.append(title)
            # urls.append(url)
            # summary.append(sum)



    # title_url_map = zip(titles, urls, summary)
    # n = 1
    # for x, y, z in title_url_map:
    #     print(str(n) + ". " + x + "\n" + y, sep="\n")  # prints each article's title, url, and summary/comment
    #     print("\n" + z + "\n")
    #     n += 1

if __name__ == '__main__':
    main()

    # urls = []
    # titles = []
    # summary = []
    #
    # for scrape in BIurls:
    #     req = requests.get(scrape)
    #     soup = BeautifulSoup(req.content, 'lxml')

    # Finds all of the titles, urls, and summaries of each article (top 3 of each URL)
    # for div in soup.find_all("div", class_="tout-text-wrapper default-tout"):
    #     a_tag = div.find("a", class_="tout-title-link")
    #     title = a_tag.text
    #     if title in titles:     #don't add articles that are already going to be added to the DB
    #         continue
    #     else:
    #         titles.append(title)
    #         if a_tag.attrs["href"][0] == "/":
    #             urls.append("https://businessinsider.com" + a_tag.attrs["href"])
    #         else:
    #             urls.append(a_tag.attrs["href"])
    #         summary_tag = div.find("div", class_="tout-text-wrapper default-tout")
    #         summary.append(summary_tag.text.strip())
    #         if summary_tag is not None:
    #             summary.append(summary_tag.text.strip())
    #         else:
    #             summary.append("No summary available for this article")

    # In order: Tech, Finance, Strategy, Retail, Executive, Prime, Intelligence, Politics, Transportation, Markets,
    # Science, News, Healthcare, Media, Enterprise, Advertising
    # BIurls = ["https://www.businessinsider.com/sai", "https://www.businessinsider.com/clusterstock",
    #           "https://www.businessinsider.com/warroom", "https://www.businessinsider.com/retail",
    #           "https://www.businessinsider.com/thelife", "https://www.businessinsider.com/prime",
    #           "https://www.businessinsider.com/research", "https://www.businessinsider.com/politics",
    #           "https://www.businessinsider.com/transportation", "https://www.businessinsider.com/moneygame",
    #           "https://www.businessinsider.com/science", "https://www.businessinsider.com/news",
    #           "https://www.businessinsider.com/healthcare", "https://www.businessinsider.com/media",
    #           "https://www.businessinsider.com/enterprise", "https://www.businessinsider.com/advertising"]
    #
    # urls = set()
    # titles = set()
    # summary = set()
    #
    # for scrape in BIurls:
    #     req = requests.get(scrape)
    #     soup = BeautifulSoup(req.content, 'lxml')
    #
    #     # Finds all of the titles, urls, and summaries of each article
    #     for div in soup.find_all("div", class_="top-vertical-trio-item"):
    #         print(div)
    #         a_tag = div.find("a", class_="tout-title-link")
    #         summary_tag = div.find("div", class_="tout-copy three-column body-regular")
    #         if a_tag.attrs["href"][0] == "/":
    #             urls.add("https://businessinsider.com" + a_tag.attrs["href"])
    #         else:
    #             urls.add(a_tag.attrs["href"])
    #         titles.add(a_tag.text)
    #         summary.add(summary_tag.text.strip())

        # for div in soup.find_all("div", class_="tout-text-wrapper default-tout"):
        #     a_tag = div.find("a")
        #     summary_tag = div.find("div")
        #     if a_tag.attrs["href"][0] == "/":
        #         urls.add("https://businessinsider.com" + a_tag.attrs["href"])
        #     else:
        #         urls.add(a_tag.attrs["href"])
        #     titles.add(a_tag.text)
        #     summary.add(summary_tag.text.strip())

    # n = 1
    # for x, y, z in zip(titles, urls, summary):
    #     print(str(n) + ". " + x + "\n" + y, sep="\n") #prints each article's title, url, and summary/comment
    #     print("\n" + z + "\n")
    #     n += 1