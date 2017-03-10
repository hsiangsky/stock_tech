#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
import matplotlib.pyplot as plt

import sys
sys.path.append('../')
from MA import MA 

stock = Stock.createByCSV('2330','../../data/2330_14MonData.csv')
ma = MA(stock)

print "MA5=> len: "+str(len(ma.ma5))
print ma.ma5
print "MA10=> len: "+str(len(ma.ma10))
print ma.ma10
print "MA20=> len: "+str(len(ma.ma20))
print ma.ma20

print "MA5 diff MA10:"+str(len(ma.ma5diffma10))
ma.printMA5DiffMA10()

#print "Buy point short term:"
#ma.printBuyPoints_ST()

#print "MA5 gradient=> len: "+str(len(ma.ma5_gradient))
#ma.printMA5_gradient()

#plt.figure(1)
#plt.subplot(211)
#plt.plot(stock.price, 'r', ma.ma5, 'b', ma.ma10, 'yellow')
#plt.ylim(min(ma.ma5[9:]), max(stock.price))
#plt.subplot(212)
#plt.plot(ma.ma5diffma10, 'g')
#plt.show()
