#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo

#
dataPath = './data/'

# Get all stock number list
stock_no_list = [i for i in sorted(TWSENo().all_stock_no)[:-2]]
print 'Total stock: '+str(len(stock_no_list))

# process
for i in stock_no_list:
  filename=dataPath+i+'.csv'
  print "Download NO."+i+" Stock 14 Mons Data to "+filename+" ..."
  stock = Stock(i,14)
  stock.out_putfile(filename)
  
