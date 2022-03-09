print("常用的查找")
a = '''我们公司确实入了6台M1Max给剪辑师，但特效师都还是AMD+3080Ti。
剪片M1Max是真的好，哪怕前天发的8K视频，剪起来也一点都不卡。
现在最大的问题是像AE和C4D的很多插件都没有兼容M1芯片，所以速度很慢。
短期内特效师还是离不开PC的。
之前答应过做一期工作流的视频，到时候可以一起讲讲影视行业对于PC还有Mac的看法'''



print(len(a))     #数字符串长度p
print(a.startswith("我们公司"))   #是不是以指定字符串开头的，做个判断
print(a.endswith("的看法"))      #是不是以指定字符串结尾的，做个判断
print(a.find("公"))             #搜索第一次出现指定字符串的位置
print(a.rfind('频'))            #搜索最后一次出现字符串的位置
print(a.count("视频"))          #计算指定字符串出现了几次
print(a.isalnum())           #所有字符串是否全是字母或者数字


print("去除首尾信息")
a = '*bai*xiao*chun*yyds*'
print(a.strip())  #去除首尾空格
print(a.strip("*"))  #去除首尾*
print(a.lstrip("*")) #去除左边*
print(a.rstrip("*")) #去除右边*

print("大小写转换")
a = "to be or not to be,welcome to BeiJing"

print(a.capitalize())   #以下均产生新的字符串，整条字符串首字母大写，其余均变小写
print(a.title())        #每个单词首字母大写
print(a.upper())        #所有字符全转成大写
print(a.lower())        #所有字符全转成小写
print(a.swapcase())     #所有字母大小写转换


print("格式排版")

a = "bair"


print(a.rjust(10,"*"))
print(a.center(10,"*"))
print(a.ljust(10,"*"))

print("其他方法")
b = '''我们公司确实入了6台M1Max给剪辑师，但特效师都还是AMD+3080Ti。
剪片M1Max是真的好，哪怕前天发的8K视频，剪起来也一点都不卡。
现在最大的问题是像AE和C4D的很多插件都没有兼容M1芯片，所以速度很慢。
短期内特效师还是离不开PC的。
之前答应过做一期工作流的视频，到时候可以一起讲讲影视行业对于PC还有Mac的看法'''

print(b.isalnum())    #是否为英文字母或数字
print(b.isalpha())    #是否只有字母组成，包含汉字
print(b.isdigit())    #是否只有数字组成
print(b.isspace())    #是否为空白符
print(b.isupper())    #是否为大写字母
print(b.islower())    #是否为小写字母

print("字符串格式化")

a = "名字是:{0},年龄是:{1}"
b = a.format("baixiaochun",26)   #{}是个占位符，里面的数字代表格式化的索引，0代表第一位，1代表第二位
print(b)
c = "名字是:{name},年龄是{age},{name}是一个好孩子"
d = c.format(name = "baixiaochun",age = 26)  #也可以通过参数名映射参数值的方法实现对字符串的格式化
print(d)


print("填充与对齐")
#^ < >分别是居中，左对齐，右对齐，后面带宽度，：后面带填充的字符，只能是一个字符，不指定默认用空格填空
a = "{:=^9}".format("245")
print(a)

f = "名字是:{name:$<16},年龄是{age:=^9},{name:*>16}是一个好孩子"  #需要在age或者name后面加填充
h = f.format(name = "baixiaochun",age = 26)
print(h)


print("数字格式化")
#浮点数通过f,整数通过d进行需要的格式化

a = "我是{0},我的存款余额有{1:.2f}"     #保留小数点后两位
b = a.format("白小纯",+5230000.567)
print(b)


c = "我是{0},我的存款余额有{1:+.2f}"     #保留小数点后两位
d = c.format("白小纯",+5230000.567)
print(d)

e = "我是{0},我的存款余额有{1:.0f}"     #不带小数，只保留整数,四舍五入
f = e.format("白小纯",+5230000.567)
print(f)

j = "我是{0},我的存款余额有{1:0>10d}"     #数字补零，填充左边，宽度为10
h = j.format("白小纯",+5230000)
print(h)

l = "我是{0},我的存款余额有{1:0<10d}"     #数字补零，填充右边，宽度为10
m = l.format("白小纯",+5230000)
print(m)

n = "我是{0},我的存款余额有{1:,}"     #以逗号隔开
o = n.format("白小纯",+5230000)
print(o)

p = "我是{0},我的存款余额有{1:.2%}"     #百分比格式
k = p.format("白小纯",+5230000.234)
print(k)

r = "我是{0},我的存款余额有{1:.2E}"     #科学计数法，指数记法
s = r.format("白小纯",+5230000)
print(s)