#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo

import sys
sys.path.append('./src')
from Rule import Rule
from Trade import Trade

# get all stock no list
stock_no_list = [i for i in sorted(TWSENo().all_stock_no)[:-2] ]
print 'Total stock: '+str(len(stock_no_list))

# parameters
contiDay_thd = 3
day = -1;

# process
for i in stock_no_list:
  try:
    stock = Stock(i)
    rule = Rule(stock)
    if rule.buyRule1(-1):
      print stock.info[0],
      print "Buy"
  
  except:
    print i
    print "[Error] "+i+" "+stock.info[0]
  
