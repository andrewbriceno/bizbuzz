from bs4 import BeautifulSoup
import requests
import csv

req = requests.get("https://www.whitehouse.gov/briefings-statements/")
soup = BeautifulSoup(req.content, 'lxml')

# #Finds the first div tag that has its class attribute specified
# res = soup.find("div", class_="briefing-statement__content").prettify()
# print(res)

#Finds all of the titles and urls of the page's briefings and statements
urls = []
titles = []

for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs["href"])
    titles.append(a_tag.text)

file = open('Briefings.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Title', 'URL'])

n = 1
for x, y in zip(titles, urls):
    print(str(n) + ". " + x + " - " + y, sep="\n") #prints each briefings title and its url
    writer.writerow([titles[n-1].strip(), urls[n-1].strip()]) #writes the titles and urls to csv excel file
    n += 1

file.close()

