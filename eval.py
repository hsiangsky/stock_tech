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
dataPath = './data/'
#stock_no_list = ['1215'] 
for no in stock_no_list[0:20]:
  #stock = Stock(no, 12)
  filename=dataPath+no+'_14MonData.csv'
  stock = Stock.createByCSV(no,filename)

  rule = Rule(stock)
  trade = Trade(stock)
  trade.initTrade()
  for i in range(rule.waitConvergeDay, rule.days):
    if rule.buyRule1(i):
      trade.buy(i)
    if rule.sellRule1(i):
      trade.sell(i)
  trade.printTradeResult()


