'''
Key things to learn in this example:

(easy)
- read .csv file
- plt.plot()
- xlabel, ylabel
- xticks, yticks
- legend
- axvline, axhline
- line width
- Chinese font

(getiing fancier)
- datetime.datetime.strptime
- two plots
- scipy.interpolate
- change background color
'''
import matplotlib.pyplot as plt
import csv
import datetime
from scipy import interpolate

target = 'temperature'
time = []
data = []

with open("BANQIAO,板橋.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    csv_format = next(reader)
    for row in reader:
        # format: 2019-05-09 01:00
        try:
            row[csv_format.index('time')].index('24:00')
            row[csv_format.index('time')] = row[csv_format.index('time')][:11] + "00:00"
        except ValueError:
            pass
        dtime = datetime.datetime.strptime(row[csv_format.index('time')], '%Y-%m-%d %H:%M')
        time.append(dtime)

        if row[csv_format.index(target)] == 'T':
            row[csv_format.index(target)] = 0.0
        else:
            row[csv_format.index(target)] = float(row[csv_format.index(target)])
        data.append(row[csv_format.index(target)])

# Data for each hour
plt.xlabel('月份(2019-2020)')
xticks, xlabels = [], []
for i in range(len(data)):
    if time[i].day == 1 and time[i].hour == 1:
        xticks.append(i)
        xlabels.append(str(time[i])[5:7])
plt.xticks(ticks=xticks, labels=xlabels)
for x in xticks:
    plt.axvline(x, lw=0.1)
plt.ylabel('溫度(°C)')
plt.plot(data, linewidth=0.3, label='逐時溫度')

# Average for each day
indexes = []
avg_data = []
avg = 0
for i in range(len(data)):
    # Average for every 24 data
    if (i+1) % 24 == 0:
        avg /= 24
        avg_data.append(avg)
        indexes.append(i)
        avg = 0
    else:
        avg += data[i]
# 1D Interpolation
spl = interpolate.InterpolatedUnivariateSpline(indexes, avg_data)
plt.plot(range(len(data)), spl(range(len(data))), label='每日平均')

# Average for the year
avg, count = 0, 0
for i in avg_data:
    avg += i
    count += 1
avg /= count
plt.axhline(avg, color='red', label='年均溫')
plt.legend()

# Cosmetics
ax = plt.gca()
ax.set_facecolor('black')

plt.show()
