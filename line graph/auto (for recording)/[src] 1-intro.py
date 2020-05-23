` 1st stage: simple plot
# 引入matplotlib函式庫裡面的pyplot，命名為plt
from matplotlib import pyplot as plt

# 手動生成一筆資料
temperature = [21, 20, 21, 23, 25, 24, 25, 25, 26, 27]

# 把資料放到圖表上
plt.plot(temperature)

# 顯示圖表
plt.show()
`
\ 2nd stage
date = ['5/1','5/2','5/3','5/4','5/5','5/6','5/7','5/8','5/9','5/10']
\ put into plt.plot()
, temperature
\ change last date
\ 3rd stage: Add labels to the axis'
plt.xlabel('日期(2020)')
plt.ylabel('溫度(攝氏)')
\ 4th stage: Add a title
plt.title('Title')
\ 5th stage: Add label for curve
, label='台北'
\ 6th stage: Show curve label
plt.legend()