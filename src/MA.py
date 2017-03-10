# -*- coding: utf-8 -*-

class MA():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.waitConvergeDay = 20
    
    # process moving average list
    self.ma5 = self.MA(5)
    self.ma10 = self.MA(10)
    self.ma20 = self.MA(20)

    # count diff
    self.ma5diffma10 = list()
    self.countDiffMA5MA10()

    # count moving average gradient list
    #self.ma5_gradient = self.countGradient(5)
    #self.ma10_gradient = self.countGradient(10)
    #self.ma20_gradient = self.countGradient(20)
 
    # alpha filter to ma gradient 
    #self.ma5_gradientSmooth = self.alphaFilter(self.ma5_gradient)

    # count buy point and sell point
    self.buyPoints_ST = []
    self.sellPoints_ST = []
    self.buyPoints_LT = []
    self.sellPoints_LT = []
    self.countBuyPoints_ST()
    self.countSellPoints_ST()
    self.countBuyPoints_LT()
    self.countSellPoints_LT()

  def MA(self, ma_day):
    res = []
    for i in range(ma_day-1):
      res.append(0)
    res.extend(self.stock.MA(ma_day)[0])
    return res

  def countGradient(self, ma_day):
    res = []
    for i in range(ma_day):
      res.append(0)
    ma_list = self.stock.MA(ma_day)[0]
    for i in range(1, len(ma_list)):
      pre_ma = ma_list[i-1]
      now_ma = ma_list[i]
      g = (now_ma-pre_ma)/pre_ma
      res.append(g)
    return res
  
  def alphaFilter(self, inList, alpha=0.8):
    res = []
    for i in range(1,len(inList)):
      res.append(inList[i-1]*(1-alpha)+inList[i]*alpha)
    return res
 
  def countDiffMA5MA10(self):
    for i in range(self.waitConvergeDay):
      self.ma5diffma10.append(0)
    for i in range(self.waitConvergeDay, len(self.ma5)):
      self.ma5diffma10.append(self.ma5[i]-self.ma10[i])

  def countBuyPoints_ST(self):
    for i in range(0,self.waitConvergeDay):
      self.buyPoints_ST.append(0)
    for i in range(self.waitConvergeDay,len(self.ma5)):
      if self.ma5[i] > self.ma10[i]:
        self.buyPoints_ST.append(1)
      else:
        self.buyPoints_ST.append(0)

  def countSellPoints_ST(self):
    for i in range(0,self.waitConvergeDay):
      self.sellPoints_ST.append(0)
    for i in range(self.waitConvergeDay,len(self.ma5)):
      if self.ma5[i] < self.ma10[i]:
        self.sellPoints_ST.append(1)
      else:
        self.sellPoints_ST.append(0)

  def countBuyPoints_LT(self):
    for i in range(0,self.waitConvergeDay):
      self.buyPoints_LT.append(0)
    for i in range(self.waitConvergeDay,len(self.ma5)):
      if self.ma10[i] > self.ma20[i]:
        self.buyPoints_LT.append(1)
      else:
        self.buyPoints_LT.append(0)

  def countSellPoints_LT(self):
    for i in range(0,self.waitConvergeDay):
      self.sellPoints_LT.append(0)
    for i in range(self.waitConvergeDay,len(self.ma5)):
      if self.ma10[i] < self.ma20[i]:
        self.sellPoints_LT.append(1)
      else:
        self.sellPoints_LT.append(0)
  
  def printBuyPoints_ST(self):
    for i in range(len(self.buyPoints_ST)):
      if self.buyPoints_ST[i] > 0:
        print "[Buy]",
        print self.stock.date[i],
        print "Price:",
        print self.stock.price[i],
        print "(ma5, ma10):",
        print str(self.ma5[i])+", "+str(self.ma10[i])
  
  def printMA5DiffMA10(self):
    for i in range(len(self.ma5)):
      print self.stock.date[i],
      print "Price:",
      print self.stock.price[i],
      print "MA5 Diff MA10:",
      print self.ma5diffma10[i]
