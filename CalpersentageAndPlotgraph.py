## Calpersentage.py
## Usage Calculate Persentage from Frequency of A T C G and Plot Percent Graph
## Disuan, Wara & Rty : dn10tenz@gmail.com
## 11/09/2013

import numpy as np
import csv, sys
import matplotlib.pyplot as plt

Tab_Delimited_File = sys.argv[1]      #Directory Tab_Delimited_File
Name_Save_Percent_File = sys.argv[2]  #Name for Save Percent Data File
Percent_Tab_File = sys.argv[3]		#Directory Percent Data File

#directory1 = 'C:/Users/hanameji/Desktop/Project/DENV1Tables.txt'
directory = Percent_Tab_File+'\\'+Name_Save_Percent_File+'.txt'     

opencsvfile = np.genfromtxt(Tab_Delimited_File, dtype=float, delimiter = '\t' ,skip_header = 1 ,usecols = (0,1,2,3,4))    ##open and read csv-files 

change_list_to_array = np.array(opencsvfile)             #Convert List to Array for calculate
sum_row = change_list_to_array.sum(axis=1)    #Sum Row Value

for j in range(0,len(sum_row)):           
	for i in range(1,5):             
		if sum_row[j] != 0:          #Because some rows is all zero.
			change_list_to_array[j,i] = np.true_divide(change_list_to_array[j,i],sum_row[j])   #Find Percentage       

#print change_list_to_array

createdfile = open(Name_Save_Percent_File+'.txt', 'w')      #Create New File 

string = '' 

for row in change_list_to_array:
	for col in row:
		L = str(col)
		string = string + L +'\t'  
		cuttab = string.strip() #cut the last tab(\t) 
	string = cuttab + '\n' 

createdfile.write(string) #write data to file
createdfile.close() 


def getColumn(directory, column):    #Get Column in Tab File
    results = csv.reader(open(directory), delimiter="\t")  #open Tab_Delimited_File
    return [result[column] for result in results]

x = getColumn(directory, 0)  #Column Position
A = getColumn(directory, 1)  #Column A
T = getColumn(directory, 2)  #Column T
C = getColumn(directory, 3)  #Column C
G = getColumn(directory, 4)  #Column G

#Del = getColumn(directory2, 5) #Column Deletion
#Ins = getColumn(directory2, 6) #Column Insertion

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
#plt.plot(x,Del,'C', label='Deletion')
#plt.plot(x,Ins,'K', label='Insertion')


#plt.savefig('figfile.png')
plt.grid(True)
plt.legend()
plt.show()
