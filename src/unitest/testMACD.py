#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo
import sys
sys.path.append('../')
from MACD import MACD

stock = Stock.createByCSV('2454', '../../data/2454_14MonData.csv')
macd= MACD(stock)
print "MACD: len: "+str(len(macd.macd))
print macd.macd
print "MACDSignal: len: "+str(len(macd.macdsignal))
print macd.macdsignal
print "MACDhist: len: "+str(len(macd.macdhist))
print macd.macdhist

print "Conti Day:"
print macd.contiDay
