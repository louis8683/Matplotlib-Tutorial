'''
Line Graph

Course Overview
- 1-intro.py
- 2-data.py
- 3-datetime.py
- 4-twolines.py
- 5-interpolate.py
- 6-beautify.py

Key things to learn in this example:

(easy)
-^ read .csv file 
-^ plt.plot()
-^ xlabel, ylabel
-^ xticks, yticks
-^ legend
- axvline, axhline
- line width
- Chinese font

(getiing fancier)
-* datetime.datetime.strptime
- two plots
- scipy.interpolate
- change background color
'''

'''Stage 1: Use datetime instead of strings'''
from matplotlib import pyplot as plt
import csv
# NOTE: Here's the Change
import datetime

date = []
temperature = []

with open("BANQIAO,板橋.csv", "r", newline='') as csv_file:
    reader = csv.reader(csv_file)
    csv_format = next(reader)
    for row in reader:
        # NOTE: Here's the Change
        try:
            date.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M"))
        except ValueError:
            row[0] = row[0].replace("24:00", "00:00")
            date.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M")+datetime.timedelta(days=1))
        temperature.append(float(row[2]))


import numpy as np


'''Stage 2: Tick with 1st day, 1st hour'''
xtick, xlabel = [], []
for i in range(len(date)):
    if date[i].day == 1 and date[i].hour == 1:
        xtick.append(i)
        xlabel.append(f"{date[i].month}")
plt.xticks(ticks=xtick, labels=xlabel)

'''Stage 3: Review, labels'''
plt.title('折線圖')
plt.xlabel('月份(2019-2020)')
plt.ylabel('溫度(攝氏)')
plt.plot(temperature, label='板橋')
plt.legend()
plt.show()
