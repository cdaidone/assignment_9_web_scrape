from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/The_Walt_Disney_Company#Revenues")
bsObj = BeautifulSoup(html, "html.parser")

t = open("scrape_project.txt", "w")

t.write("sales_rev = [")


rows = bsObj.find("table", {"class":"wikitable"}).findAll("tr")
for index in range (1, len(rows)):
    t.write("{")
    row = rows[index].findAll("th")
    years = row[0]
    years.sup.clear()
    t.write("'Year:'%r," % years.get_text())
    row2 = rows[index].findAll("td")
    revenue = row2[2]
    t.write("'Revenue:'%r" % revenue.get_text())
    t.write("},\n")
t.write("]")


t.close()

#How it is now: only get 1991 (twice) and 2700. Nothing else.
#When I tried to create a dict, "3" was not recognized.
