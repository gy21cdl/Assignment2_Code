# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:51:27 2022

@author: Chris Lambert
"""

#Imported modules
import pandas as pd

#open csv file using pandas
#create a data fame variable (df)
df = pd.read_csv (r'D:\UniversityOfLeeds\Year1\GEOG5003M_ProgrammingForGeographicalInformationAnalysis\Assignment2_Code\Assignment2_RawData_v2.csv')   
#print (df) #print check


y  = {'f(x)': [2,4,6,8], 'g(x)':[4,2,-2,6]}
x = [1,2,3,4]

graph = pd.DataFrame(y,x)
graph.plot(kind='line',grid = True, title='My Graph',ylabel='my y title',xlabel ='my x title')
