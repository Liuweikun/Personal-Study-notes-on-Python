print("可变字符串")
#需要频繁修改字符串，但是每次用replace太麻烦

import io

s = "hello ,world"  #原字符串
sio = io.StringIO(s)   #新生成的对象,值和s的一样
print(sio.getvalue())

sio.seek(7)       #指针定位到从左往右第7个位置
sio.write("W")    #将这个位置的字符串修改

print(sio.getvalue())   
