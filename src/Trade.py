# -*- coding: utf-8 -*-
import numpy as np
import math

class Trade():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.initTrade()

  def initTrade(self):
    self.tradeBuy = list()
    self.tradeSell = list()
    self.tradeCost = 0
    self.net = 0
    self.hold = 0

  def KD_PerfectBuy_HighestKSell(self, KD):
    self.initTrade()
    for i in range(KD.waitConvergeDay, len(KD.k)):
      if KD.perfectBuyPoints[i]:
        self.buy(i)
      if KD.k[i] < KD.k[i-1] and KD.k[i] > 65:
        self.sell(i) 

  def buy(self, idx):
    buyPrice = self.stock.price[idx]
    self.tradeCost += buyPrice
    self.net -= buyPrice
    self.hold += 1
    self.tradeBuy.append((self.stock.date[idx], buyPrice))

  def sell(self, idx):
    # trade sell
    if self.hold > 0:
      sellPrice = self.stock.price[idx]
      self.net += sellPrice
      self.hold -= 1
      self.tradeSell.append((self.stock.date[idx], sellPrice))


  def printTradeResult(self):
    if self.tradeCost == 0:
      return
    self.__printStockInfo()
    print ""
    for i in range(len(self.tradeBuy)):
      print "[Buy]" ,
      print self.tradeBuy[i]
    for i in range(len(self.tradeSell)):
      print "[Sell]" ,
      print self.tradeSell[i]

    if self.hold != 0:
      print "Hold "+str(self.hold), 
      print ", sell price: "+str(self.stock.price[-1])
      self.net += self.stock.price[-1]*self.hold
    print "[Total Profit]" + str(round(self.net/self.tradeCost, 4))
#    self.__printTradeTotalProfit()

  def printTradeFail(self):
    for i in range(len(self.tradeProfit)):
      if self.tradeProfit[i][1] < 0:
        print "[TradeFail]",
        self.__printStockInfo()
        self.__printDeal(i)
  
  def __printStockInfo(self):
    print self.stock.info[0].rjust(10),

  def __printDeal(self, idx):
    print "[Buy]",
    print self.tradeBuy[idx],
    print "[Sell]",
    print self.tradeSell[idx],
    print "[Profit]",
    print "("+("%.2f"%self.tradeProfit[idx][0])+", "+ \
      ("%.2f"%(self.tradeProfit[idx][1]*100))+"%)"

  def __printTradeTotalProfit(self):
    totalProfit = 0
    for i in range(self.trade_counter):
      totalProfit += self.tradeProfit[i][0]
    print "[Total Profit] "+str(totalProfit)

  def KD_isTodayPerfectBuyPoint(self, KD):
    if KD.perfectBuyPoints[-1]:
      print "[Buy]",
      self.__printStockInfo()
      self.__printPrice(-1)
      self.__printKD(KD, -1)
      return True
    else:
      return False

  def KD_isTodayPerfectSellPoint(self, KD):
    if KD.perfectSellPoints[-1]:
      print "[Sell]",
      self.__printStockInfo()
      self.__printPrice(-1)
      self.__printKD(KD, -1)
      return True
    else:
      return False

  def __printPrice(self, idx):
    print "Price: "+("%6.2f"%self.stock.price[idx]).rjust(9),

  def __printKD(self, KD, idx):
    print "(K,D): ("+("%3.2f"%KD.k[idx]).rjust(6)+", "+("%3.2f"%KD.d[idx]).rjust(6)+")"
