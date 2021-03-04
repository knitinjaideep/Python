#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:22:56 2020

@author: nitinkotcherlakota
"""

import xlwings as xw
import bs4 as bs
import requests


@xw.func
def get_stock(ticker,args =[]):
    url_base = 'https://ca.finance.yahoo.com/quote/'
    src_base = requests.get(url_base+ticker).text
    src_profile = requests.get(url_base+ticker+r'/profile?p=' + ticker).text
    soup = bs.BeautifulSoup(src_base,'lxml')
    soup_profile = bs.BeautifulSoup(src_profile, 'lxml')
    

    try:
        div_info = soup.find('td',attrs={'data-test':'DIVIDEND_AND_YIELD-value'}).get_text()
        div_amt = div_info.split(' ')[0]
        div_pct = div_info.split(' ')[1].split('(')[1].split(')')[0]
    except:
        div_info = soup.find('td',attrs={'data-test':'TD_YIELD-value'}).get_text()
        div_amt = 'N/A'
        div_pct = div_info

    try:
        s_eps = soup.find('td',attrs={'data-test':'EPS_RATIO-value'}).get_text()
    except:
        s_eps = 'N/A'


    try:
        er_dt = soup.find('td',attrs={'data-test':'EARNINGS_DATE-value'}).get_text()
    except:
        er_dt = 'N/A'

    try:
        ex_div_dt = soup.find('td',attrs={'data-test':'EX_DIVIDEND_DATE-value'}).get_text()
    except:
        ex_div_dt = 'N/A'

    try:
        mkt_cap = soup.find('td', attrs={'data-test' : 'MARKET_CAP-value'}).get_text()
    except:
        mkt_cap = soup.find('td', attrs={'data-test' : 'NET_ASSETS-value'}).get_text()

        
    s_attrs = {'Co. Name' : soup.find_all('h1')[0].get_text().split(' - ')[1],
               'Price' : soup.find_all('div',attrs={'id':'quote-header-info'})[0].find(attrs={'data-reactid':'14'}).get_text(),
               'Volume' : soup.find('td',attrs={'data-test':'TD_VOLUME-value'}).get_text(),
               'Trailing PE' : soup.find('td',attrs={'data-test':'PE_RATIO-value'}).get_text(),
               'Trailing EPS' : s_eps,
               'Earning Date' : er_dt,
               'Dividend Amount' : div_amt,
               'Dividend %' : div_pct,
               'Ex Dividend Date' : ex_div_dt,
               'Market Cap' : mkt_cap,
               'Sector' : soup_profile.find('span', attrs ={'data-reactid' : '21'}).get_text(),
               }

    return [s_attrs[attr] for attr in args if attr in s_attrs]