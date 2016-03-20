
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://allears.net/tix/tixincrease.htm")
bsObj = BeautifulSoup(html, "html.parser")

t = open("pricetable.txt", "w")

t.write("prices = [")

rows = bsObj.find("table", {"class":"tix"}).findAll("tr")
for index in range (1, len(rows)):
    t.write("{")
    row = rows[index].findAll("td")
    date = row[0].get_text()
    t.write("%r," % date)
    one_day_price = row[1].get_text()
    t.write("%r," % one_day_price)
    one_day_increase = row[2].get_text()
    t.write("%r," % one_day_increase)
    annual_price = row[3].get_text()
    t.write("%r," % annual_price)
    annual_increase = row[4].get_text()
    t.write("%r," % annual_increase)
    prem_annual_price = row[5].get_text()
    t.write("%r," % prem_annual_price)
    prem_annual_increase = row[6].get_text()
    t.write("%r," % prem_annual_increase)
    comments = row[7].get_text()
    t.write("%r," % comments)
    t.write("},\n")
t.write("]")


t.close()
