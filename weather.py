# -*- coding: utf-8 -*-
"""
Ouputs actual temp for the days of the month that have passed and forecasted 
for the the days that have not yet passed.
"""

from bs4 import BeautifulSoup
import requests


def table(website):
    soup = BeautifulSoup(website.text, 'html.parser')
    info = soup.findAll('tr', {'span': 'wx-value'})
    results = '{}'
    print info
    for row in info:
        row = row.findAll('span')
        print row
        for each in row:
            print each

            

if __name__ == '__main__':
    link  = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
    website = requests.get(link)
    print '%57s' % 'Weather'
    print '=' * 66
    data = table(website)