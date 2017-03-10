#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grs import Stock
from grs import TWSENo
import sys
sys.path.append('../')
from DMI import DMI

stock = Stock.createByCSV('2454', '../../data/2454_14MonData.csv')
dmi = DMI(stock)
print "dmi +DI: len: "+str(len(dmi.plus_di))
print dmi.plus_di
print "dmi -DI: len: "+str(len(dmi.minus_di))
print dmi.minus_di
print "dmi adx: len: "+str(len(dmi.adx))
print dmi.adx

print "Conti Day:"
print dmi.contiDay
