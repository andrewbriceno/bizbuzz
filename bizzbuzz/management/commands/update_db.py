from datetime import datetime, time, timedelta
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from bizzbuzz.models import News
import requests

class Command(BaseCommand):
    def purge_db(self):
        a_week_ago = datetime.now() - timedelta(days=7)
        News.objects.filter(expiration_date__contains=a_week_ago).delete()

    def add_forbes_articles(self):
        # add rows for articles that are not already in the database
        req = requests.get('https://www.forbes.com/business')
        soup = BeautifulSoup(req.content, features='html.parser')

        # replaces punctuation with space so companies can be parsed
        punctuations = '''!()-[]{};:\'\"\\”“’’‘‘,<>./?@#$%^&*_~'''
        translator = str.maketrans(punctuations, ' ' * len(punctuations))

        # master list of companies we track
        company_master_list = ['AMAZON', 'SAMSUNG', 'IBM', 'TWITTER', 'NETFLIX',
                               'ORACLE', 'SAP', 'SALESFORCE', 'TESLA', 'SPACEX',
                               'MICROSOFT', 'APPLE', 'GOOGLE', 'FACEBOOK']

        # finds each article
        articles = soup.findAll('h2')

        for article in articles:
            if article.a is not None:
                url = article.a['href']
                hit = str(News.objects.filter(url=url)) #Check if URL is already in DB
                if "<News: News object" in hit:     #Article is already in DB, so skip adding it
                    continue
                else:           #Add article to DB
                    req = requests.get(url)
                    soup = BeautifulSoup(req.content, features='html.parser')
                    first_para = soup.find('div', class_="article-body-container")
                    if first_para is None:
                        continue
                    sum = first_para.find('p').text
                    title = soup.find('title').text
                    new_title = title.translate(translator)
                    company_check = set(company_master_list).intersection(new_title.upper().split(' '))
                    if company_check:
                        article = News(title=title, url=url, summary=sum, company=company_check)
                        article.save()

    def add_BI_articles(self):
        BIurls = ["https://www.businessinsider.com/sai", "https://www.businessinsider.com/clusterstock",
                  "https://www.businessinsider.com/warroom", "https://www.businessinsider.com/retail",
                  "https://www.businessinsider.com/thelife", "https://www.businessinsider.com/prime",
                  "https://www.businessinsider.com/research", "https://www.businessinsider.com/politics",
                  "https://www.businessinsider.com/transportation", "https://www.businessinsider.com/moneygame",
                  "https://www.businessinsider.com/science", "https://www.businessinsider.com/news",
                  "https://www.businessinsider.com/media", "https://www.businessinsider.com/enterprise"]

        punctuations = '''!()-[]{};:\'\"\\”“’’‘‘,<>./?@#$%^&*_~'''
        translator = str.maketrans(punctuations, ' ' * len(punctuations))

        company_master_list = ['AMAZON', 'SAMSUNG', 'IBM', 'TWITTER', 'NETFLIX',
                               'ORACLE', 'SAP', 'SALESFORCE', 'TESLA', 'SPACEX',
                               'MICROSOFT', 'APPLE', 'GOOGLE', 'FACEBOOK']
        for scrape in BIurls:
            req = requests.get(scrape)
            soup = BeautifulSoup(req.content, 'lxml')

            for div in soup.find_all("div", class_="top-vertical-trio-item"):
                a_tag = div.find("a", class_="tout-title-link")
                title = a_tag.text
                if a_tag.attrs["href"][0] == "/":
                    url = "https://businessinsider.com" + a_tag.attrs["href"]
                else:
                    url = a_tag.attrs["href"]

                hit = str(News.objects.filter(url=url))
                if "<News: News object" in hit:
                    continue    #don't add urls that are already in the DB or already going to be added
                else:
                    sum = div.find("div", class_="tout-copy three-column body-regular").text.strip()
                    new_title = title.translate(translator)
                    company_check = set(company_master_list).intersection(new_title.upper().split(' '))
                    if company_check:
                        article = News(title=title, url=url, summary=sum, company=company_check)
                        article.save()

    def add_NYT_articles(self):
        NYTurls = ["https://www.nytimes.com/section/technology", "https://www.nytimes.com/section/business",
                   "https://www.nytimes.com/section/business/economy",
                   "https://www.nytimes.com/section/business/energy-environment",
                   "https://www.nytimes.com/section/science", "https://www.nytimes.com/section/science/space"]

        # replaces punctuation with space so companies can be parsed
        punctuations = '''!()-[]{};:\'\"\\”“’’‘‘,<>./?@#$%^&*_~'''
        translator = str.maketrans(punctuations, ' ' * len(punctuations))

        company_master_list = ['AMAZON', 'SAMSUNG', 'IBM', 'TWITTER', 'NETFLIX',
                               'ORACLE', 'SAP', 'SALESFORCE', 'TESLA', 'SPACEX',
                               'MICROSOFT', 'APPLE', 'GOOGLE', 'FACEBOOK']

        urls = []

        for scrape in NYTurls:
            req = requests.get(scrape)
            soup = BeautifulSoup(req.content, 'lxml')

            for div in soup.find_all("li", class_="css-ye6x8s"):
                a_tag = div.find("a")
                title = a_tag.find("h2").text
                if a_tag.attrs["href"][0] == "/":
                    url = "https://nytimes.com" + a_tag.attrs["href"]
                else:
                    url = a_tag.attrs["href"]

                hit = str(News.objects.filter(url=url))
                if "<News: News object" in hit:
                    continue    #don't add urls that are already in the DB or already going to be added
                else:
                    sum = a_tag.find("p")
                    if not sum:
                        continue
                    sum = sum.text
                    new_title = title.translate(translator)
                    company_check = set(company_master_list).intersection(new_title.upper().split(' '))
                    if company_check:
                        article = News(title=title, url=url, summary=sum, company=company_check)
                        article.save()

    def add_TT_articles(self):
        # Tech, Science, Business, Features
        TTurls = ["https://www.techtimes.com/personaltech", "https://www.techtimes.com/science",
                  "https://www.techtimes.com/biztech", "https://www.techtimes.com/feature"]

        # replaces punctuation with space so companies can be parsed
        punctuations = '''!()-[]{};:\'\"\\”“’’‘‘,<>./?@#$%^&*_~'''
        translator = str.maketrans(punctuations, ' ' * len(punctuations))

        company_master_list = ['AMAZON', 'SAMSUNG', 'IBM', 'TWITTER', 'NETFLIX',
                               'ORACLE', 'SAP', 'SALESFORCE', 'TESLA', 'SPACEX',
                               'MICROSOFT', 'APPLE', 'GOOGLE', 'FACEBOOK']
        for scrape in TTurls:
            req = requests.get(scrape)
            soup = BeautifulSoup(req.content, 'lxml')

            for div in soup.find_all("div", class_="list2"):
                a_tag = div.find("h2").find("a")
                url = a_tag.attrs["href"]
                hit = str(News.objects.filter(url=url))
                if "<News: News object" in hit:
                    continue    #don't add urls that are already in the DB or already going to be added
                else:
                    title = a_tag.text
                    p_tag = div.find("p", class_="summary")
                    sum = p_tag.text
                    new_title = title.translate(translator)
                    company_check = set(company_master_list).intersection(new_title.upper().split(' '))
                    if company_check:
                        article = News(title=title, url=url, summary=sum, company=company_check)
                        article.save()

    def handle(self, *args, **options):
        self.purge_db()
        self.add_forbes_articles()
        self.add_BI_articles()
        self.add_NYT_articles()
        self.add_TT_articles()