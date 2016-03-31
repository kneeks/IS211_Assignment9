# -*- coding: utf-8 -*-
"""
Outputs the close price and date for all dates shown on the webpage
"""

from bs4 import BeautifulSoup
import requests

def table(website):
    soup = BeautifulSoup(website.text, 'html.parser')
    info = soup.findAll('tr')
    results = 'Date: {:^13}| Close: {:^7}'
    for row in info:
        row = row.findAll('td', {'class': 'yfnc_tabledata1'})
        if len(row) == 7:   
            print results.format(row[0].contents[0], row[6].contents[0])



if __name__ == '__main__':
    link  = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"
    website = requests.get(link) 
    print '%24s' % 'Apple Stock Data'
    print '=' * 34
    data = table(website)