#Project

#Step 1: Reading CSV File:
#Read the content from the provided data.csv file and print the contents.
import csv
file = open('/Users/duyanhnguyen/Downloads/Sem 2/ITM 200/Project/Data.csv','r')
fCSV = csv.reader(file)
#for line in fCSV:
#    print(f'{line}')


#Step 2: Total Sale
#Calculate the number of total vehicles sold in each year starting from 2012 to 2021.
#Write this information in a text file called stats.txt.
file1 = open('/Users/duyanhnguyen/Downloads/Sem 2/ITM 200/Project/Stats.csv','w')
sales = []
yr = []
total = []
year = 2012
count = 1
for a in fCSV:
    sales.append(a)
file1.write(f'Year-Sum\n')
while count < 12:
    sum1 = 0
    for b in sales[count]:
        if int(b) == year: continue
        else:
            sum1 += int(b)
    file1.write(f'{year}-{sum1}\n')
    yr.append(year)                 #For step 3
    total.append(sum1)               #For step 3
    year += 1
    count += 1
file1.write(f'\n')

#Step 3: Bar Plot
#Plot the total sales for each year (2012 to 2021) using bar() plot.
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

file2 = open('/Users/duyanhnguyen/Downloads/Sem 2/ITM 200/Project/Stats.csv','r')
y= [total[0],total[1],total[2],total[3],total[4],total[5],total[6],total[7],total[8],total[9],total[10]]
x= [yr[0],yr[1],yr[2],yr[3],yr[4],yr[5],yr[6],yr[7],yr[8],yr[9],yr[10]]

plt.figure(1)
plt.bar(x,y)
plt.title("Total automotive sales in Canada per year from 2012 to 2022")
plt.xlabel("Year")
plt.ylabel("CAD")
plt.ticklabel_format(style='plain', axis='y')
plt.show()


#Step 4: Sale Estimation
#Calculate total sales in first 6 months of 2021
#Calculate total sales in first 6 months of 2022
#Calculate the sales growth rate for the first 6 months of 2022
#Write down the calculated sales growth rate value in the stats.txt file.
#Based on the calculated growth rate (SGR) estimate the sales in each month
#for the last six months (Jul to Dec) of 2022.

sales21 = sales[10]; sales22 = sales[11]
halfSales21 = sales21[1:7]; halfSales22 = sales22[1:7]
intHalfSales21 = [int(x) for x in halfSales21]
file1.write(f'Total sales - first half 2021: {sum(intHalfSales21)}\n')
intHalfSales22 = [int(x) for x in halfSales22]
file1.write(f'Total sales - first half 2022: {sum(intHalfSales22)}\n')
sgr = (sum(intHalfSales22)-sum(intHalfSales21))/sum(intHalfSales22)
file1.write(f'Sales Growth Rate 22-21: {round(sgr,2)}\n')

file1.write(f'\n')

est22 = []
predHalfSales21 = sales21[7:13]
intPredHalfSales21 = [int(x) for x in predHalfSales21]
month = 7
file1.write('Est. sales 2022\n')
for d in intPredHalfSales21:
    file1.write(f'Month {month} 2022: {round(d+d*sgr,2)}\n')
    est22.append(round(d+d*sgr,2))                              #for step 5
    month += 1

file1.write(f'\n')

#Step 5: Horizontal Bar Plot
#Plot the estimated sales for the last six months of 2022 using barh() plot.

y= [est22[0],est22[1],est22[2],est22[3],est22[4],est22[5]]
x= ['July','August','September','October','November','December']

plt.figure(1)
plt.barh(x,y)

plt.title("Estimated Sales - Q3/4 - 2022")
plt.xlabel("CAD")
plt.ylabel("Month")
plt.grid()
plt.show()

file.close()
file1.close()
file2.close()