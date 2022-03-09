print("时间的表示")
#1970年1月1日 00:00:00开始，以1毫秒（1/1000秒）前进计算，此时间点为unix时间点

import time
a = time.time()  #代表获取当前时刻，单位是秒，
print(a)

b = int(a)
totalMinute = b/60
totalhours = totalMinute/60
totaldays = totalhours/24
totalyears = totaldays/356
print(int(totalMinute))
print(int(totaldays))
print(int(totalhours))
print(int(totalyears))
thisyear = 1970 + int(totalyears)
print("今年为"+ str(thisyear) + "年")   #str将指定的值转化为字符串




