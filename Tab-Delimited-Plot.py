## Tab-Delimited-Plot.py
## Usage for create graph from Dengue Virus Tab-Delimited File
## Disuan, Wara and Rty : dn10tenz@gmail.com
## 05/09/13

import csv, os, sys
import matplotlib.pyplot as plt
import numpy as np

Tab_Delimited_File = sys.argv[1] #Directory Dengue Virus Tab-Delimited FIle

def getColumn(Tab_Delimited_File, column):    #Get Column in Tab File
    results = csv.reader(open(Tab_Delimited_File), delimiter="\t")  #open Tab_Delimited_File
    headers = results.next()  #Cut First Row(Header)
    return [result[column] for result in results]

x = getColumn(Tab_Delimited_File, 0)  #Column Position
A = getColumn(Tab_Delimited_File, 1)  #Column A
T = getColumn(Tab_Delimited_File, 2)  #Column T
C = getColumn(Tab_Delimited_File, 3)  #Column C
G = getColumn(Tab_Delimited_File, 4)  #Column G
Del = getColumn(Tab_Delimited_File, 5) #Column Deletion
Ins = getColumn(Tab_Delimited_File, 6) #Column Insertion

length_axes_X = len(x)    #length of X-Axes

print('Size of X-Axes is 1-%i Positions' %length_axes_X)    #Show Length of X-Axes
x_size_start = input('Please Choose Axes X Start from = ') #Choose X-Axes Start 
x_size_end = input('Please Choose Axes X End to = ')  #Choose X-Axes End

plt.xlim(x_size_start,x_size_end)   

plt.xlabel('Position (X)')
plt.ylabel('Frequency (Y)')
plt.title('Dengue Virus')

plt.plot(x,A,'R', label='A')
plt.plot(x,T,'Y', label='T')
plt.plot(x,C,'B', label='C')
plt.plot(x,G,'M', label='G')
plt.plot(x,Del,'C', label='Deletion')
plt.plot(x,Ins,'K', label='Insertion')


plt.savefig('figfile.png')
plt.grid(True)
plt.legend()
plt.show()

    

