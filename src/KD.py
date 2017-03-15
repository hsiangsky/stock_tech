# -*- coding: utf-8 -*-
from talib import abstract as ta
import numpy as np
import util
class KD():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.rsv = list() 
    self.k = list() 
    self.d = list()
    self.k_threshold = 80
    self.d_threshold = 20
    self.perfectBuyPoints = list()
    self.perfectSellPoints = list()
    self.normalBuyPoints = list() # normal golden point
    self.normalSellPoints = list() # normal dead point

    ta.STOCH.parameters = {
        'fastk_period' : 5, 
        'slowk_period' : 3, 
        'slowk_matype' : 1, 
        'slowd_period' : 3, 
        'slowd_matype' : 1
      }

    self.__countKD()

    # count buy point and sell point
    self.countPerfectBuyPoints()
    self.countPerfectSellPoints()
    self.countNormalBuyPoints()
    self.countNormalSellPoints()

    self.contiDay=util.countContiDay(self.normalBuyPoints)
  
  def __countKD(self):
    self.k, self.d = ta.STOCH(self.stock.inputs)

  def isBuyPoint(self, i):
    return (self.k[i] > self.d[i] and self.k[i-1] < self.d[i-1])

  def isSellPoint(self, i):
    return (self.k[i] < self.d[i] and self.k[i-1] > self.d[i-1])
   

  def printInfo(self):
    for i in range(len(self.stock.date)):
      print self.stock.date[i],
      print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

  def countPerfectBuyPoints(self):
    self.perfectBuyPoints.append(0)
    for i in range(1, len(self.k)):
      if self.k[i] > self.d[i] and self.k[i-1] < self.d[i-1] and self.d[i] < self.d_threshold:
        self.perfectBuyPoints.append(1)
      else:
        self.perfectBuyPoints.append(0)
  
  def countNormalBuyPoints(self):
    self.normalBuyPoints.append(0)
    for i in range(1, len(self.k)):
      if self.k[i] > self.d[i] and self.k[i-1] < self.d[i-1]:
        self.normalBuyPoints.append(1)
      else:
        self.normalBuyPoints.append(0)

  def printPerfectBuyPoints(self):
    for i in range(0, len(self.k)):
      if self.perfectBuyPoints[i]:
        print "[Buy]",
        print self.stock.info[0].rjust(10),
        print self.stock.date[i],
        print "Price: "+("%6.2f"%self.stock.price[i]).rjust(9),
        print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

  def countPerfectSellPoints(self):
    self.perfectSellPoints.append(0)
    for i in range(1, len(self.k)):
      if self.k[i] < self.d[i] and self.k[i-1] > self.d[i-1] and self.k[i] > self.k_threshold:
        self.perfectSellPoints.append(1)
      else:
        self.perfectSellPoints.append(0)

  def countNormalSellPoints(self):
    self.normalSellPoints.append(0)
    for i in range(1, len(self.k)):
      if self.k[i] < self.d[i] and self.k[i-1] > self.d[i-1]:
        self.normalSellPoints.append(1)
      else:
        self.normalSellPoints.append(0)
  
  def printPerfectSellPoints(self):
    for i in range(0, len(self.k)):
      if self.perfectSellPoints[i]:
        print "[Sell]",
        print self.stock.info[0].rjust(10),
        print self.stock.date[i],
        print "Price: "+("%6.2f"%self.stock.price[i]).rjust(9),
        print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

