# -*- coding: utf-8 -*-
import math
def countContiDay(diff):
  contiDay = list()
  for i in range(len(diff)):
    if math.isnan(diff[i]):
      contiDay.append(float('nan'))
    elif i is 0:
      if diff[i] > 0:
        contiDay.append(1)
      else:
        contiDay.append(-1)
    elif diff[i] > 0:
      if contiDay[i-1] > 0:
        contiDay.append(contiDay[i-1]+1)
      else:
        contiDay.append(1)
    else:
      if contiDay[i-1] < 0:
        contiDay.append(contiDay[i-1]-1)
      else:
        contiDay.append(-1)
  return contiDay        


