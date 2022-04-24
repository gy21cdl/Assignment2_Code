# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:46:00 2022

@author: Chris Lambert
"""

#Imported modules
import pandas as pd
import matplotlib.pyplot as plt

#open csv file using pandas
#create a data fame variable (df)
df = pd.read_csv (r'D:\UniversityOfLeeds\Year1\GEOG5003M_ProgrammingForGeographicalInformationAnalysis\Assignment2_Code\Assignment2_RawData_v2.csv')   
#print (df) #print check


# Define data series
y = df['Au_ppm']
x = df['Sample No']

#if df['Sample Type'] == 'BLK'
    

graph = pd.DataFrame(y,x)
graph.plot(kind='line',grid = True, title='Plot of Blank Samples for Au ppm',ylabel='my y title',xlabel ='my x title')

plt.show()
