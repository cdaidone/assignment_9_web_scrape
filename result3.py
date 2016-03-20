import csv
from collections import OrderedDict

prices = OrderedDict[{'Oct 1971','$3.50','\xa0','\xa0','\xa0','\xa0','\xa0','General admission price at opening of Magic Kingdom',},
{'Feb 1972','$3.75','$.25','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Apr 1973','$4.50','$.75','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Jun 1974','$5.25','$.75','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Dec 1975','$6.00','$.75','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'1976','$6.00','No Increase','\xa0','\xa0','\xa0','\xa0','No ticket prices raised in 1976',},
{'Jun 1977','$6.00','No Increase','\xa0','\xa0','\xa0','\xa0','All tickets raised except General Admission',},
{'Jun 1978','$6.50','$.50','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Apr 1979','$7.00','$.50','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Mar 1980','$7.50','$.50','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Nov 1980','$8.00','$.50','\xa0','\xa0','\xa0','\xa0','2nd price increase of the year',},
{'Oct 1981','$9.50','$1.50','\xa0','\xa0','\xa0','\xa0','General Admission replaced by One Day Ticket in 1981',},
{'Jun 1982','$13.25','$3.75','\xa0','\xa0','\xa0','\xa0','\xa0',},
{'Sep 1982','$15.00','$1.75','$100','\xa0','\xa0','\xa0','2nd increase of 1982. Annual Pass introduced.',},
{'Oct 1983','$17.00','$2.00','$125','$25','\xa0','\xa0','\xa0',},
{'Feb 1984','$17.00','No Increase','$125','No Increase','\xa0','\xa0','Only minor gates (RC & DI) increased',},
{'Jun 1984','$18.00','$1.00','$135','$10','\xa0','\xa0','\xa0',},
{'Jun 1985','$19.50','$1.50','$140','$5','\xa0','\xa0','\xa0',},
{'Nov 1985','$21.50','$2.00','$140','No Increase','\xa0','\xa0','2nd increase of 1985',},
{'Mar 1986','$23.00','$1.50','$140','No Increase','\xa0','\xa0','\xa0',},
{'Jun 1986','$24.50','$1.50','$155','$15','\xa0','\xa0','2nd increase of 1986',},
{'Dec 1986','$26.00','$1.50','$155','No Increase','\xa0','\xa0','3rd increase of 1986',},
{'Dec 1987','$28.00','$2.00','$165*','$10','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'May 1988','$28.00','No Increase','$165*','No Increase','\xa0','\xa0','Only selected tickets were increased. *Add RC & DI to AP for $10 more',},
{'May 1989','$29.00','$1.00','$180*','$15','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'Feb 1990','$31.00','$2.00','$180*','No Increase','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'Feb 1991','$33.00','$2.00','$189*','$9','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'Jun 1992','$34.00','$1.00','$190*','$10','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'May 1993','$35.00','$1.00','$199*','$9','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'Mar 1994','$36.00','$1.00','$199*','No Increase','\xa0','\xa0','*Add RC & DI to AP for $10 more',},
{'Nov 1994','$36.00','No Increase','$205','$6','$319','\xa0','2nd increase of 1994. Premium Annual Pass introduced.',},
{'Feb 1995','$37.00','$1.00','$205','No Increase','$319','No Increase','\xa0',},
{'Dec 1995','$37.00','No Increase','$220','$15','$319','No Increase','\xa0',},
{'Feb 1996','$38.50','$1.50','$220','No Increase','$319','No Increase','\xa0',},
{'Oct 1996','$38.50','No Increase','$236','$16','$329','$10','\xa0',},
{'Mar 1997','$39.75','$1.25','$269','$33','$359','$30','\xa0',},
{'Sep 1997','$39.75','No Increase','$288','$19','$389','$30','\xa0',},
{'Apr 1998','$42.00','$2.25','$288','No Increase','$389','No Increase','\xa0',},
{'Sep 1998','$42.00','No Increase','$299','$10','$399','$10','\xa0',},
{'May 1999','$44.00','$2.00','$299','No Increase','$399','No Increase','\xa0',},
{'Oct 1999','$44.00','No Increase','$309','$10','$415','$16','\xa0',},
{'Jan 2000','$46.00','$2.00','$324','$15','$434','$19','\xa0',},
{'Jan 2001','$48.00','$2.00','$349','$25','$469','$35','\xa0',},
{'Sep 2002','$50.00','$2.00','$369','$20','$489','$20','\xa0',},
{'Jun 2003','$52.00','$2.00','$369','No Increase','$489','No Increase','\xa0',},
{'Feb 2004','$52.00','No Increase','$369','No Increase','$489','No Increase','Disney raised Ultimate Park Hopper Prices only',},
{'Mar 2004','$54.75','$2.75','$379','$10','$499','$10','\xa0',},
{'Oct 2004','$54.75','No Increase','$379','No Increase','$499','No Increase','Disney raised single day admission to water parks and DQ only',},
{'Jan 2005','$59.75','$5.00','$395','$16','$515','$16','Magic Your Way Base ticket (one day-one park) replaced One Day park tickets',},
{'Jan 2006','$63.00','$3.25','$415','$20','$539','$24','\xa0',},
{'Aug 2006','$67.00','$4.00','$434','$19','$559','$20','2nd increase of 2006',},
{'Aug 2007','$71.00','$4.00','$448','$14','$579','$20','\xa0',},
{'Aug 2008','$75.00','$4.00','$469','$21','$599','$20','\xa0',},
{'May 2009','$75.00','No Increase','$469','No Increase','$599','No Increase','Disney raised single day admission to water parks only',},
{'Aug 2009','$79.00','$4.00','$489','$20','$619','$20','\xa0',},
{'Aug 2010','$82.00','$3.00','$499','$10','$629','$10','\xa0',},
{'Jun 2011','$85.00','$3.00','$519','$20','$649','$20','\xa0',},
{'Jun 2012','$89','$4','$574','$55','$699','$50','\xa0',},
{'Jun 2013','$95 - MK$90 - other theme parks','$6 - $1','$609','$35','$729','$30','Disney offered 1 day tickets for Magic Kingdom at $95 adult and 1 day tickets for Epcot, Animal Kingdom or Hollywood Studios at $90 adult.',},
{'Feb 2014','$99 - MK$94 - other theme parks','$4','$634','$25','$754','$25','\xa0',},
{'Feb 2015','$105 - MK$97 - other theme parks','$6 - $3','$659','$25','$779','$25','Florida Resident Annual Pass (both the regular and Premium) were raised by $44 each',},
{'Oct 2015','No Increase','No Increase','$749','$90','$829','$50','Disney increased annual passes only. Annual Pass became Platinum Pass while Premium Annual Pass became Platinum Plus Pass.',},
{'Feb 2016','$124 Peak$110 Regular$105 Value','$19 Peak$5 Regular$0 Value','No Increase','No Increase','No Increase','No Increase','Disney goes to a tiered pricing model on one day tickets.',},
{'\xa0','\xa0','\xa0','\xa0','\xa0','\xa0','\xa0','\xa0',},
]
sales_rev = OrderedDict[{'Year:''1991','Revenue:''2,794.0'},
{'Year:''1992','Revenue:''3,306'},
{'Year:''1993','Revenue:''3,440.7'},
{'Year:''1994[65][66]','Revenue:''3,463.6'},
{'Year:''1995[65][66]','Revenue:''3,959.8'},
{'Year:''1996[67]','Revenue:''4,142[Rev 3]'},
{'Year:''1997','Revenue:''5,014'},
{'Year:''1998','Revenue:''5,532'},
{'Year:''1999','Revenue:''6,106'},
{'Year:''2000','Revenue:''6,803'},
{'Year:''2001','Revenue:''6,009'},
{'Year:''2002','Revenue:''6,691'},
{'Year:''2003','Revenue:''6,412'},
{'Year:''2004','Revenue:''7,750'},
{'Year:''2005','Revenue:''9,023'},
{'Year:''2006','Revenue:''9,925'},
{'Year:''2007','Revenue:''10,626'},
{'Year:''2008','Revenue:''11,504'},
{'Year:''2009','Revenue:''10,667'},
{'Year:''2010','Revenue:''10,761'},
{'Year:''2011','Revenue:''11,797'},
{'Year:''2012','Revenue:''12,920'},
{'Year:''2013','Revenue:''14,087'},
{'Year:''2014','Revenue:''15,099'},
]

result = OrderedDict()

csvFile = open('my_data.csv', 'w')
try:
    writer = csv.writer(csvFile)
    writer.writerow(['Date', '1 Day Price', '1 Day Increase', 'Annual Price', 'Annual Increase', 'Prem. Annual Price', 'Prem. Annual Increase', 'Comments', 'Revenue'])
    for key, value in result.iteritems():
        w.writerow([key] + value)
    #writer.writerows((prices))
    #writer.writerows((sales_rev))
finally:
    csvFile.close()

    #w = csv.DictWriter(f, dicts)
    #w.writerows(dicts)

#f.close()
