import random


print("列表的排序")
a = [20,10,60,30,40] 
print(id(a))
a.sort()              #升序排列
print(a)
print(id(a))   #证明排序不影响列表的唯一性

a.sort(reverse=True)  #降序排列
print(a)

random.shuffle(a)   #导入random模块，打乱顺序排序
print(a)
random.shuffle(a)
print(a)


print("建立新的列表排序")
a = [20,30,10,40]
print(id(a))
a = sorted(a)
print(a)
print(id(a))   #通过sorted(a)时，会建立新的对象
a = sorted(a,reverse = True)
print(a)      #通过sorted进行降序排列

print("实现逆序排列")
a = [10,20,30,40]
print(a[::-1])   #方法一
c = reversed(a)  #方法二，通过reversed进行逆序排列
print(c)         #翻转迭代器只能用一次，第二次就失效了 
print(c)

print("函数的小方法，Max和min")
a = [10,3,8,20,56]
print(max(a))    #返回最大最小值
print(min(a))
print(sum(a))    #求和

print("二维列表")
a = [
        ["陈妍宇",25,30000,"北京"],
        ["曹亚雄",25,30000,"上海"],
        ["齐哲颖",25,30000,"广州"],
        
]
for m in range(3):
    for n in range(4):
        print(a[m][n],end="\t")
    print() 
