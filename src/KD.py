# -*- coding: utf-8 -*-
import util
class KD():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.rsv = list() 
    self.k = list() 
    self.d = list()
    self.perfectBuyPoints = list()
    self.perfectSellPoints = list()
    self.normalBuyPoints = list() # normal golden point
    self.normalSellPoints = list() # normal dead point
    self.waitConvergeDay = 40
    self.tradeBuy = dict()
    self.tradeSell = dict()
    self.tradeProfit = dict() 

    # init first 8 day as zero
    for i in range(8):
      self.k.append(50)
      self.d.append(50)
      self.rsv.append(0)
    
    # process kd list
    for i in range(8,len(self.stock.price)):
      self.RSV(i)
      self.KD(i)
    
    # count buy point and sell point
    self.countPerfectBuyPoints()
    self.countPerfectSellPoints()
    self.countNormalBuyPoints()
    self.countNormalSellPoints()

    self.contiDay=util.countContiDay(self.normalBuyPoints)
  
  def RSV(self, idx, sample=9):
    price_min = min(self.stock.lowestPrice[idx+1-sample:idx+1])
    price_max = max(self.stock.highestPrice[idx+1-sample:idx+1])
    price = self.stock.price[idx]
    if (price_max - price_min) != 0:
      self.rsv.append((price-price_min)/(price_max-price_min)*100)
    else:
      print "[Error] RSV divide by zero",
      print self.stock.info[0],
      print self.stock.date[i]
      exit(1)

  def KD(self, idx):
    self.k.append((2.0*self.k[idx-1] + self.rsv[idx])/3)
    self.d.append((2.0*self.d[idx-1] + self.k[idx])/3)

  def printInfo(self):
    for i in range(len(self.stock.date)):
      print self.stock.date[i],
      print "RSV:",
      print ("%3.2f" % self.rsv[i]).rjust(6),
      print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

  def countPerfectBuyPoints(self):
    # wait about 2 mons for KD convergence
    for i in range(0,self.waitConvergeDay):
      self.perfectBuyPoints.append(0)
    for i in range(self.waitConvergeDay,len(self.k)):
      if self.k[i] > self.d[i] and self.d[i] < 20:
        self.perfectBuyPoints.append(1)
      else:
        self.perfectBuyPoints.append(0)
  
  def countNormalBuyPoints(self):
    # wait about 2 mons for KD convergence
    for i in range(0,self.waitConvergeDay):
      self.normalBuyPoints.append(0)
    for i in range(self.waitConvergeDay,len(self.k)):
      if self.k[i] > self.d[i]:
        self.normalBuyPoints.append(1)
      else:
        self.normalBuyPoints.append(0)

  def printPerfectBuyPoints(self):
    for i in range(self.waitConvergeDay, len(self.k)):
      if self.perfectBuyPoints[i]:
        print "[Buy]",
        print self.stock.info[0].rjust(10),
        print self.stock.date[i],
        print "Price: "+("%6.2f"%self.stock.price[i]).rjust(9),
        print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

  def countPerfectSellPoints(self):
    # wait about 2 mons for KD convergence
    for i in range(0,self.waitConvergeDay):
      self.perfectSellPoints.append(0)
    for i in range(self.waitConvergeDay, len(self.k)):
      if self.k[i] < self.d[i] and self.d[i] > 80:
        self.perfectSellPoints.append(1)
      else:
        self.perfectSellPoints.append(0)

  def countNormalSellPoints(self):
    # wait about 2 mons for KD convergence
    for i in range(0,self.waitConvergeDay):
      self.normalSellPoints.append(0)
    for i in range(self.waitConvergeDay, len(self.k)):
      if self.k[i] < self.d[i]:
        self.normalSellPoints.append(1)
      else:
        self.normalSellPoints.append(0)
  
  def printPerfectSellPoints(self):
    for i in range(self.waitConvergeDay, len(self.k)):
      if self.perfectSellPoints[i]:
        print "[Sell]",
        print self.stock.info[0].rjust(10),
        print self.stock.date[i],
        print "Price: "+("%6.2f"%self.stock.price[i]).rjust(9),
        print "(K,D): ("+("%3.2f"%self.k[i]).rjust(6)+", "+("%3.2f"%self.d[i]).rjust(6)+")"

