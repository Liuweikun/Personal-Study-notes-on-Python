print("切片操作")
a = [10,20,30,40,50,60,70]
print(a[:])           #提取整个列表
print(a[1:0])         #提取从start索引到结尾
print(a[:-1])         #从头开始直到末尾前一位
print(a[1:3])         #从索引1到3的元素
print(a[1:5:2])       #索引1到5之间的元素，步长为2
print(a[-3:])         #索引倒数第三个到结尾
print(a[-5:-3])       #倒数第5个到倒数第3个，包头不包尾
print(a[::-1])        #步长为负，从右到左反向提取
  