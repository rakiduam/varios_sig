# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:44:39 2020

@author: fneir
"""


import time

year, month, day, hour, minute, sec, wday, yday, isdst = time.localtime()

print('inicio:', ('.').join([str(year),str(month).zfill(2), str(day).zfill(2)]),  (':').join([str(hour), str(minute)]))
