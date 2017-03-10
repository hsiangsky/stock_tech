#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo

import sys
sys.path.append('../')
from Trade import Trade
from KD import KD 
from MA import MA
from DMI import DMI
from MACD import MACD

stock = Stock.createByCSV('2454', '../../data/2454_14MonData.csv')
trade = Trade(stock)
dmi = DMI(stock)
macd = MACD(stock)
print "MACD with adx >16:"
trade.MACD_DMI_1(macd, dmi)
trade.printTradeResult()

kd = KD(stock)
#print "Trade by perfect buy and perfect sell KD:"
#trade.KD_PerfectBuyPerfectSell(kd)
#trade.printTradeResult()
#print "Trade by perfect buy and normal sell KD:"
#trade.KD_PerfectBuyNormalSell(kd)
#trade.printTradeResult()
#print "Trade by normal buy and normal sell KD:"
#trade.KD_NormalBuyNormalSell(kd)
#trade.printTradeResult()
print "Trade by perfect buy and highest k sell KD:"
trade.KD_PerfectBuy_HighestKSell(kd)
trade.printTradeResult()
#
#ma = MA(stock)
#print "Trade by short term MA:"
#trade.MA_ST(ma)
#trade.printTradeResult()
#
#print "Trade by short term Diff MA:"
#trade.MA_ST_diff(ma)
#trade.printTradeResult()
#print "Trade by long term MA:"
#trade.MA_LT(ma)
#trade.printTradeResult()
