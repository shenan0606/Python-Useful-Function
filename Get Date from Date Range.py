# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:57:59 2019

@author: SW010056
"""

from datetime import datetime, timedelta
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step
        
for d in date_range(datetime(2019, 9, 1), datetime(2019,10,1), timedelta(days=1)):
    print(str(d)[:10])