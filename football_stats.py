# -*- coding: utf-8 -*-
"""
Outputs a list of top 20 players, including the players position, team and
total number of touchdowns.
"""

from bs4 import BeautifulSoup
import requests


def table(website):
    soup = BeautifulSoup(website.text, 'html.parser')
    info = soup.findAll(class_ = {'row1','row2'})
    results = 'Player: {:^20}| Position: {:^3}| Team: {:^4}| TD\'s {:^3}'
    for row in info[0:20]:
        print results.format(row.contents[0].text, row.contents[1].text, 
                             row.contents[2].text, row.contents[6].text)


if __name__ == '__main__':
    link  = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns'
    website = requests.get(link)
    print '%57s' % 'Here is a list of the top 20 players in the NFL.'
    print '=' * 66
    data = table(website)