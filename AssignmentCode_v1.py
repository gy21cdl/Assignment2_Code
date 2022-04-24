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


################################################
'''
#Sample Stats
count_samp_all = df['Sample No'].count()
max_samp_all = df['Sample No'].max()
min_samp_all = df['Sample No'].min()
mean_Au_all = df['Au_ppm'].mean()
mean_Cu_all = df['Cu_ppm'].mean()
mean_Pb_all = df['Pb_ppm'].mean()
mean_Zn_all = df['Zn_ppm'].mean()

print("Total number of samples equals"+" "+str(count_samp_all))
print("Maximum sample number is"+" "+str(max_samp_all))
print("Minimum sample number is"+" "+str(min_samp_all))
print("Mean Au value is"+" "+str(mean_Au_all))
print("Mean Cu value is"+" "+str(mean_Cu_all))
print("Mean Pb value is"+" "+str(mean_Pb_all))
print("Mean Zn value is"+" "+str(mean_Zn_all))

count_samp_type = df.groupby(['Sample Type']).count()
print ("Count of values, grouped by the Sample Type:" + str(count_samp_type))

#https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
'''
###################################################


#Plot 1 - All data
#Use rcParams to refine the plot size
from matplotlib import rcParams
rcParams['figure.figsize'] = 10,8 #increase figure size

# Define data series and axis
x = df['X_m']
y = df['Y_m']
#plt.xlim(297500,312500) #axis value limits if required
#plt.ylim() #axis value limits if required
#plt.xticks([300000,304000,308000]) #limiting axis plot
#plt.yticks([4,4.04,4.08]) #limiting axis plot - not working atm

# Define graph features
plt.title("Geographical Plot of All Data")
plt.xlabel("X_UTM") #x axis label
plt.ylabel("Y_UTM") #y axis label
plt.grid(True,color='k', linestyle=':') #plot grid 
plt.legend(loc=2) # legend and location - not currently working for this

# Define data Subset
#plt.scatter(x, y, color = 'red') #single colour plot
#fig, ax = plt.subplots()
#colors = {'BLK':'red', 'DUP':'green', 'CRM':'blue', 'NRM':'yellow'}
#grouped = df.groupby('Sample Type')
#for key, group in grouped:
#    group.plot(ax=ax, kind='scatter', grid=True, x=('X_m'), y=('Y_m'), label=key, color=colors[key])

plt.subplot()
grouped = df.groupby('Sample Type')
colors = {'BLK':'red', 'DUP':'green', 'CRM':'blue', 'NRM':'yellow'}


plt.show()

#y  = {'f(x)': [2,4,6,8], 'g(x)':[4,2,-2,6]}
#x = [1,2,3,4]

#graph = pd.DataFrame(y,x)
#graph.plot(kind='scatter',grid = True, title='My Graph',ylabel='my y title',xlabel ='my x title')


########################################################



