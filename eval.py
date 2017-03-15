#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo

import sys
sys.path.append('./src')
from Rule import Rule
from Trade import Trade

# get all stock no list
stock_no_list = [i for i in sorted(TWSENo().all_stock_no)[:-2]]
print 'Total stock: '+str(len(stock_no_list))

# process
dataPath = '/home/hsiangsky/stock/data/all_stk/'
#stock_no_list = ['2023'] 
for no in stock_no_list:
#  stock = Stock(no, 15)
  filename=dataPath+no+'.csv'
  stock = Stock.createByCSV(no,filename)

  rule = Rule(stock)
  trade = Trade(stock)
  trade.initTrade()
  for i in range(rule.days):
    if rule.buyRule_kd_cci(i):
      trade.buy(i)
    if rule.sellRule_kd_cci(i):
      trade.sell(i)
  trade.printTradeResult()


