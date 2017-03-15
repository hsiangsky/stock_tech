# -*- coding: utf-8 -*-
#from talib.abstract import *
from talib import abstract as ta
import numpy as np
import util

class MACD():
  def __init__(self, stockObj):
    self.stock = stockObj
    
    # setting parameters
    ta.MACD.parameters = {
        'fastperiod'   : 12, 
        'slowperiod'   : 26, 
        'signalperiod' : 20
        }
    self.__countMACD()
    self.contiDay=util.countContiDay(self.macdhist)

  def __countMACD(self):
    self.macd, self.macdsignal, self.macdhist = \
        ta.MACD(self.stock.inputs)

  def isBuyPoint(self, idx):
    if idx < 4:
      return False
    return (self.macdhist[idx] > 0 and self.macdhist[idx-4] < 0)

  def isSellPoint(self, idx):
    if idx < 4:
        return False
    return (self.macdhist[idx] < 0 and self.macdhist[idx-4] < 0)
