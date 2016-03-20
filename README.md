***INTRODUCTION***
For this project, I wanted to scrape the data detailing the change in ticket prices at Walt Disney World since October 1971 to February 2016 and comparing it to the overall revenue for the year.
First, I got the url for the site with the ticket data, http://allears.net/tix/tixincrease.htm, and then I got the URL for the site with the Revenue data https://en.wikipedia.org/wiki/The_Walt_Disney_Company#Revenues.
I located the the tags I wanted to target using Developer Tools on Chrome.
I used a virtual environment in Terminal.
All files: web_scrape.py, pricetable.py, web_scrape3.py, scrape_project.py

***STEP 1: TICKET PRICE SCRAPE***
To scrape the ticket price site (web_scrape.py):
1. Import BeautifulSoup
2. Open URL
3. Get BeautifulSoup to parse and assign bsObj.
4. Open the file the info will be stored, pricetable.py
5. First thing written to pricetable.py, the name of the dictionary: "prices" and start dictionary.
6. Created a variable (rows) that is assigned to the function that finds the first table on the page with the class "tix" and findAll rows (tr).
7. Created a for loop that writes the { and runs through each row, getting the date, various prices, increases, and comments according to their index position [0,1,2,3 etc].
8. Before each row is run through, the loop checks each row and finds all <td>. The results are stored to their respective variable.
9. After a row is scanned, the text is grabbed, stored to its respective variable and written to the file: pricetable.py.
10. At the end, a line break is added so that the next row is added in a line of its own.
11. This continues for all table entries.
12. pricetable.py is closed.

***STEP 2: REVENUE SCRAPE***
To scrape the revenue table (web_scrape3.py):
Same as above except the dictionary name is sales_rev and it finds the table with the class "wikitable" and all table headers <th> are found then scrapped. A specific tag, sup, is also cleared before being written to the file: scrape_project.py.
Then all table rows <tr> are found, stored, and written to the file scrape_project.py.
The loop ends and the file is closed.

***STEP 3: WRITE TO CSV***
In results3.py, this was my biggest challenge. I found error after error when trying to import the pricetable.py and scrape_project.txt so a quick solution was to copy and paste the complete dictionaries named prices and sales_rev.
Then the file my_data.csv was opened/created, the variable writer was assigned to the function csv.writer(csvFile). csvFile is the variable for the opened file.
A row is written for the column headers, I repeatedly got an error for .writeheaders so I resorted to .writerow.

The next row(s) to be written were the actual table data, originally I had prices and sales_rev saved to one variable like: dicts=(prices, sales_rev), but that bunched everything together in the csv file.
My solution was to call each table/dictionary seperatly like writer.writerows((prices)) and writer.writerrows((sales_rev)). This inputed the data into the CSV as I had wanted. Although the revenue data is below prices, I adjusted so that "Year" and "Revenue" appeared before their respective data.
Finally, the file is closed and saves to my_data.csv.

***CHALLENGES***
Another challenge was trying to preserve the order of the data, despite many articles online detailing OrderedDict, I repeatedly received errors in Terminal.
As of right now, I have yet to figure it out, but I'm determined! Biggest problem: finding recent info since it has changed over time. A lot of it also seemed above my head in regard to understanding. If only .sort() or sorted was what I needed!
***I've included a file that shows the OrderedDict how it was shown multiple times online, but I could never get it to work - that is result3_withorderdict.py***.

I was so happy when I figured out how to get the dictionaries on the csv! It might not be in order, but I did get it there!

Another bizarre problem was that .get_text() would not work in web_scrape3.py like it did in web_scrape.py, by playing around I discovered that if I moved .get_text() to where the info is actually written to the file instead when assigned to a variable, the text was grabbed.
