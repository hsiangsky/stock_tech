# -*- coding: utf-8 -*-
from talib import abstract as ta
import numpy as np
import util

class DMI():
  def __init__(self, stockObj):
    self.stock = stockObj

    # setting parameters
    ta.ADX.parameters = {
        'timeperiod'   : 14
        }
    ta.PLUS_DI.parameters = {
        'timeperiod'   : 14
        }
    ta.MINUS_DI.parameters = {
        'timeperiod'   : 14
        }
    self.__countDMI()

    # count contiDay
    self.contiDay = util.countContiDay(self.plus_di-self.minus_di)

  def __countDMI(self):
    self.adx = ta.ADX(self.stock.inputs)
    self.plus_di = ta.PLUS_DI(self.stock.inputs)
    self.minus_di = ta.MINUS_DI(self.stock.inputs)


