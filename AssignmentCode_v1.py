# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:51:27 2022

@author: Chris Lambert
"""

#Imported modules
import pandas as pd
import matplotlib.pyplot as plt

#open csv file using pandas
#create a data fame variable (df)
df = pd.read_csv (r'D:\UniversityOfLeeds\Year1\GEOG5003M_ProgrammingForGeographicalInformationAnalysis\Assignment2_Code\Assignment2_RawData_v2.csv')   
#print (df) #print check


#Plot all data
from matplotlib import rcParams
rcParams['figure.figsize'] = 10,8 #increase figure size
x = df['X_m']
y = df['Y_m']
#plt.legend(loc=2) # legend and location - not currently working for this
plt.grid(True,color='k', linestyle=':') #plot grid 
plt.title("Geographical Plot of All Data")
plt.xlabel("X_UTM") #x axis label
plt.ylabel("Y_UTM") #y axis label
#plt.xlim(297500,312500) #axis value limits if required
#plt.ylim() #axis value limits if required
plt.xticks([300000,304000,308000]) #limiting axis plot
#plt.yticks([4,4.04,4.08]) #limiting axis plot - not working atm
plt.scatter(x, y, color = 'red')
plt.show()

#y  = {'f(x)': [2,4,6,8], 'g(x)':[4,2,-2,6]}
#x = [1,2,3,4]

#graph = pd.DataFrame(y,x)
#graph.plot(kind='scatter',grid = True, title='My Graph',ylabel='my y title',xlabel ='my x title')
