# -*- coding: utf-8 -*-
from talib import abstract as ta
import numpy as np
import util

class AROON():
  def __init__(self, stockObj, timeperiod=14):
    self.stock = stockObj
    self.strong = 90
    self.stable = 16

    ta.AROON.parameters = {
        'timeperiod' : timeperiod
      }
    ta.AROONOSC.parameters = {
        'timeperiod' : timeperiod
      }

    self.__countAROON()

  def __countAROON(self):
    self.aroondown, self.aroonup = ta.AROON(self.stock.inputs)
    self.aroonosc = ta.AROONOSC(self.stock.inputs)

  def isStrongUp(self, idx):
    return (self.aroonup[idx] > self.strong)

  def isStrongDown(self, idx):
    return (self.aroondown[idx] > self.strong)

  def isUpEnough(self, idx):
    return (self.aroonosc[idx] > self.stable)
 
  def isDownEnough(self, idx):
    return (self.aroonosc[idx] < -1*self.stabel)

  def setStrongIdx(self, parameter):
    self.strong = parameter

  def setStableIdx(self, parameter):
    self.stable = paramater

