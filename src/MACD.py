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
        'signalperiod' : 9
        }
    self.__countMACD()
    self.contiDay=util.countContiDay(self.macdhist)

  def __countMACD(self):
    self.macd, self.macdsignal, self.macdhist = \
        ta.MACD(self.stock.inputs)

