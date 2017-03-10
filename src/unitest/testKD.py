#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo

import sys
sys.path.append('../')
from KD import KD 

stock = Stock('2330',12)
kd = KD(stock)
kd.printInfo()

print "\nPrint Perfect Buy Points:"
kd.printPerfectBuyPoints()

print "\nIs Today Perfect Buy Point?"
if not kd.isTodayPerfectBuyPoint():
  print "  NO!"

print "\nPrint Perfect Sell Points:"
kd.printPerfectSellPoints()

print "\nIs Today Perfect Sell Point?"
if not kd.isTodayPerfectSellPoint():
  print "  NO!"


