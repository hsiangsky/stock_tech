# -*- coding: utf-8 -*-
from talib import abstract as ta
import numpy as np
import util

class CMO():
  def __init__(self, stockObj, timeperiod=14):
    self.stock = stockObj
    self.high = 42
    self.low = -26

    ta.CCI.parameters = {
        'timeperiod' : timeperiod
      }

    self.__countCMO()


  def __countCMO(self):
    self.cmo = ta.CMO(self.stock.inputs)

  def isOverBuy(self, idx):
    return (self.cmo[idx] > self.high)

  def isOverSell(self, idx):
    return (self.cmo[idx] < self.low)
 
  def enterOverBuy(self, idx):
    return (self.isOverBuy(idx) and not self.isOverBuy(idx-1))

  def leaveOverBuy(self, idx):
    return (not self.isOverBuy(idx) and self.isOverBuy(idx-1))

  def enterOverSell(self, idx):
    return (self.isOverSell(idx) and not self.isOverSell(idx-1))

  def leaveOverSell(self, idx):
    return (not self.isOverSell(idx)  and self.isOverSell(idx-1))

  def setHigh(self, high):
    self.high = high

  def setLow(self, low):
    self.low = low
