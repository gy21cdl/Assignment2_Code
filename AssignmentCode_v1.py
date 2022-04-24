# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:51:27 2022

@author: Chris Lambert
"""

import pandas as pd

y  = {'f(x)': [2,4,6,8]}
x = [1,2,3,4]

graph = pd.DataFrame(y,x)
graph.plot(kind='line',grid = True, title='My Graph',ylabel='my y title',xlabel ='my x title')
