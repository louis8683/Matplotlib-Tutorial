'''
Line Graph

Course Overview
- 1-intro.py
- 2-data.py
- 3-average.py
- 4-interpolate.py
- 5-beautify.py

Key things to learn in this example:

(easy)
- read .csv file 
-* plt.plot()
-* xlabel, ylabel
-* xticks, yticks
-* legend
- axvline, axhline
- line width
- Chinese font

(getiing fancier)
- datetime.datetime.strptime
- two plots
- scipy.interpolate
- change background color
'''

'''Stage 1: Show a Line Graph'''
from matplotlib import pyplot as plt

temperature = [21, 20, 21, 23, 25, 24, 25, 25, 26, 27]

#plt.plot(temperature)
#plt.show()

'''Stage 2: Change the x-axis'''
date = ['5/1','5/2','5/3','5/4','5/5','5/6','5/7','5/8','5/9','5/10']
 
#plt.plot(date, temperature)
#plt.show()

'''Notes for changeing the x-axis'''
#date = ['5/1','5/2','5/3','5/4','5/5','5/6','5/7','5/8','5/9','5/1']

'''Stage 3: Add a label to the axis'''
plt.xlabel('日期(2020)')
plt.ylabel('溫度(攝氏)')

#plt.show()

'''Stage 4: Add a title to the graph'''
plt.title('Title')
#plt.show()

'''Stage 5: Add a name to the curve'''
plt.plot(date, temperature, label='台北')
#plt.show()

'''Stage 6: Show the name of the curve'''
plt.legend()
plt.show()
