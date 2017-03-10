# -*- coding: utf-8 -*-
import numpy as np
import math

class Trade():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.initTrade()

  def initTrade(self):
    self.tradeBuy = dict()
    self.tradeSell = dict()
    self.tradeProfit = dict() 
    self.trade_counter = 0
    self.buy_lock = False

  def KD_PerfectBuy_HighestKSell(self, KD):
    self.initTrade()
    for i in range(KD.waitConvergeDay, len(KD.k)):
      if KD.perfectBuyPoints[i]:
        self.__Buy(i)
      if KD.k[i] < KD.k[i-1] and KD.k[i] > 65:
        self.__Sell(i) 

  def buy(self, idx):
    if self.buy_lock == False:
      buyPrice = self.stock.price[idx]
      self.tradeBuy[self.trade_counter] = \
          (self.stock.date[idx], buyPrice)
      self.buy_lock = True

  def sell(self, idx):
    if self.buy_lock == True:
      # don't buy sell the same date
      buyDate = self.tradeBuy[self.trade_counter][0]
      isTodayBuy = buyDate == self.stock.date[idx]
      if isTodayBuy:
        return

      # trade sell
      sellPrice = self.stock.price[idx]
      self.tradeSell[self.trade_counter] = \
          (self.stock.date[idx], sellPrice)
      # count Profit
      buyPrice = self.tradeBuy[self.trade_counter][1]
      profit = sellPrice-buyPrice
      percentage = round(profit/buyPrice,4)
      self.tradeProfit[self.trade_counter] = (profit, percentage)
      # set control parameters
      self.buy_lock = False
      self.trade_counter+=1

  def printTradeResult(self):
    self.__printStockInfo()
    print ""
    for i in range(len(self.tradeProfit)):
      self.__printDeal(i)
    self.__printTradeTotalProfit()

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
