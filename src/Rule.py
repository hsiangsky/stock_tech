# -*- coding: utf-8 -*-
from KD import KD
from MACD import MACD
from DMI import DMI
from AROON import AROON
from CCI import CCI
from CMO import CMO

class Rule():
  def __init__(self, stockObj):
    self.stock = stockObj
    self.kd = KD(stockObj)
    self.macd = MACD(stockObj)
    self.dmi = DMI(stockObj)
    self.aroon = AROON(stockObj)
    self.cci = CCI(stockObj)
    self.cmo = CMO(stockObj)
    self.days = len(self.kd.k)

  def __initFlag(self):
    self.isKD = 0
    self.isKD_30 = 0
    self.isKD_65 = 0
    self.isKD_70 = 0
    self.isKD_80 = 0
    self.isKD_turnRight = 0
    self.isMACD = 0
    self.isMACD_005 = 0
    self.isMACD_010 = 0
    self.isMACD_020 = 0
    self.isMACD_grow = 0
    self.isDMI = 0
    self.isDMI_020 = 0
    self.isDMI_grow = 0
    self.isVolume = 0
    self.isPrice = 0
    self.isDay_min = 0
    self.isDay_max2 = 0
    self.isDay_max = 0

  def __skipRule(self, i):
    if self.stock.volume[i] < 1000:
        #self.dmi.adx[i] < 18:
      return True
    else:
      return False

  def buyRule_kd_cci(self, i):
    return (self.kd.isBuyPoint(i) and self.cci.isOverSell(i))

  def sellRule_kd_cci(self, i):
    return (self.kd.isSellPoint(i) and self.cci.isOverBuy(i))

  def buyRule_kd_cmo(self, i):
    return (self.kd.isBuyPoint(i) and self.cmo.isOverSell(i))

  def sellRule_kd_cmo(self, i):
    return (self.kd.isSellPoint(i) and self.cmo.isOverBuy(i))

  def buyRule_cci(self, i):
    return self.cci.leaveOverSell(i)

  def sellRule_cci(self, i):
    return (self.cci.enterOverBuy(i) or self.cci.leaveOverBuy(i))

  def buyRule_cmo(self, i):
    return self.cmo.leaveOverSell(i)

  def sellRule_cmo(self, i):
    return (self.cmo.enterOverBuy(i) or self.cmo.leaveOverBuy(i))

  def buyRule_macd_aroon(self, i):
    return (self.aroon.isStrongUp(i) and self.aroon.isUpEnough() \
            and self.macd.isBuyPoint(i))

  def sellRule_macd_aroon(self, i):
    return (self.aroon.isStrongDown(i) and self.aroon.isDownEnough() \
            and self.macd.isSellPoint(i))


  def buyRule1(self, i):
    if self.__skipRule(i):
      return False
    self.__countBuyRule(i)

    if (self.isKD or \
        self.isKD_turnRight) and \
        self.isKD_30 and \
        self.isMACD_010 and \
        self.isDMI and \
        self.isDay_min:
      return True
    else:
      return False
  
  def buyRule2(self, i):
    if self.__skipRule(i):
      return False
    self.__countBuyRule(i)

    if self.isKD and \
        self.kd.contiDay[i] < 3 and \
        self.kd.k[i] < 40 and \
        self.isMACD_020 and \
        self.isMACD_grow:
      return True
    else:
      return False

  def sellRule1(self, i):
    self.__countSellRule(i)
    if self.isKD:
      return True
    else:
      return False

  def __countBuyRule(self,i):
    self.__initFlag()
    if self.kd.k[i] > self.kd.d[i]:
      self.isKD = 1
    if self.kd.k[i] > self.kd.d[i-1] and \
        self.kd.k[i-1] < self.kd.k[i-2] and \
        self.kd.k[i] < 50:
      self.isKD_turnRight = 1
    if self.kd.k[i] < 80:
      self.isKD_80 = 1
    if self.kd.k[i] < 70:
      self.isKD_70 = 1
    if self.kd.k[i] < 65:
      self.isKD_65 = 1
    if self.kd.k[i] < 30:
      self.isKD_30 = 1
    if self.macd.macdhist[i] > 0:
      self.isMACD = 1
    if self.macd.macdhist[i] > (-0.05):
      self.isMACD_005 = 1
    if self.macd.macdhist[i] > (-0.1):
      self.isMACD_010 = 1
    if self.macd.macdhist[i] > (-0.2):
      self.isMACD_020 = 1
    if self.macd.macdhist[i] > self.macd.macdhist[i-1]:
      self.isMACD_grow = 1
    if self.dmi.plus_di[i] > self.dmi.minus_di[i]:
      self.isDMI = 1
    if (self.dmi.plus_di[i]-self.dmi.minus_di[i]) > (-2):
      self.isDMI_020 = 1
    if (self.dmi.plus_di[i]-self.dmi.minus_di[i]) > \
        (self.dmi.plus_di[i-1]-self.dmi.minus_di[i-1]):
      self.isDMI_grow = 1
    if self.stock.volume[i] > 1.5*self.stock.volume[i-1]:
      self.isVolume = 1
    if self.stock.price[i] > 1.015*self.stock.price[i-2]:
      self.isPrice = 1
    if min(self.kd.contiDay[i], self.macd.contiDay[i], \
        self.dmi.contiDay[i]) < 2:
      self.isDay_min = 1
    if max(self.kd.contiDay[i], self.macd.contiDay[i], \
        self.dmi.contiDay[i]) < 5:
      self.isDay_max = 1
    if max(self.kd.contiDay[i], self.macd.contiDay[i], \
        self.dmi.contiDay[i]) < 3:
      self.isDay_max2 = 1
  
  def __countSellRule(self, i):
    self.__initFlag()
    if self.kd.k[i] < self.kd.d[i] and \
        self.kd.k[i] < 75:
      self.isKD = 1
    if self.macd.macdhist[i] < (0.2):
      self.isMACD_020 = 1
    if self.macd.macdhist[i] < self.macd.macdhist[i-1]:
      self.isMACD_grow = 1
    if (self.dmi.plus_di[i] < self.dmi.minus_di[i]):
      self.isDMI = 1
    if self.stock.volume[i] > 1.5*self.stock.volume[i-1]:
      self.isVolume = 1
    if self.stock.price[i] < 1.015*self.stock.price[i-2]:
      self.isPrice = 1
