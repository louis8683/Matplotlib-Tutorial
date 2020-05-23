'''
Line Graph

Course Overview
- 1-intro.py
- 2-data.py
- 3-datetime.py
- 4-twolines.py
    - interpolate
    - beautify.py

Key things to learn in this example:

(easy)
-^ read .csv file 
-^ plt.plot()
-^ xlabel, ylabel
-^ xticks, yticks
-^ legend
-* axvline, axhline
-* line width
- Chinese font

(getiing fancier)
-^ datetime.datetime.strptime
-* two plots
-* scipy.interpolate
- change background color
'''

from matplotlib import pyplot as plt
import csv
import datetime

date = []
temperature = []

with open("BANQIAO,板橋.csv", "r", newline='') as csv_file:
    reader = csv.reader(csv_file)
    csv_format = next(reader)
    for row in reader:
        try:
            date.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M"))
        except ValueError:
            row[0] = row[0].replace("24:00", "00:00")
            date.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M")+datetime.timedelta(days=1))
        temperature.append(float(row[2]))


import numpy as np


xtick, xlabel = [], []
for i in range(len(date)):
    if date[i].day == 1 and date[i].hour == 1:
        xtick.append(i)
        xlabel.append(f"{date[i].month}")
plt.xticks(ticks=xtick, labels=xlabel)

plt.title('折線圖')
plt.xlabel('月份(2019-2020)')
plt.ylabel('溫度(攝氏)')
plt.plot(temperature, label='逐時觀測')

'''Stage 1: make another set of data'''
average = []
addup = 0
for i in range(len(temperature)):
    addup += temperature[i]
    if i % 24 == 23:
       average.append(addup/24)
       addup = 0

'''Stage 2: plt.plot'''
#plt.plot(average, label='日均溫')

# NOTE: data is not aligned

'''Stage 2: interpolate'''
from scipy import interpolate


indexes = []
for i in range(len(temperature)):
    if i % 24 == 23:
        indexes.append(i)

spline = interpolate.InterpolatedUnivariateSpline(indexes, average)
#plt.plot(spline(range(len(temperature))), label='日均溫')

'''Stage 3: Beautify'''
plt.plot(spline(range(len(temperature))), label='日均溫', linewidth=2)
for x in xtick:
    plt.axvline(x, lw=0.1)

plt.legend()
plt.show()
