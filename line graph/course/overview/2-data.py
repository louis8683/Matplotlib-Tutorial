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
-* read .csv file 
-^ plt.plot()
-^ xlabel, ylabel
-* xticks, yticks
-^ legend
- axvline, axhline
- line width
- Chinese font

(getiing fancier)
- datetime.datetime.strptime
- two plots
- scipy.interpolate
- change background color
'''

'''Stage 1: Read from a cvs file'''
from matplotlib import pyplot as plt
import csv

date = []
temperature = []

with open("BANQIAO,板橋.csv", "r", newline='') as csv_file:
    reader = csv.reader(csv_file)
    csv_format = next(reader)
    for row in reader:
        date.append(row[0])
        temperature.append(float(row[2]))

#plt.plot(date, temperature, label='板橋')
#plt.show()

# Note: This should break (too many string comparisons)
# Note: temperature must be casted into a float

'''Stage 2: ticks'''
import numpy as np
xtick = np.linspace(0,len(date)-1, num=10, dtype=int)
xlabel = []
for tick in xtick:
    xlabel.append(date[tick])

plt.xticks(ticks=xtick, labels=xlabel)
plt.plot(temperature, label='板橋')
plt.show()
