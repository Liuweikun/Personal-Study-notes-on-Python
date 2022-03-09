print("字符串")
#python3使用Unicode字符串，可以表示任何书面语言的字符

a = 'baixiaochun'
b = "I'm a teacher"  #字符串单引号双引号均可以
c = '''kuaile shi 
baixiaochun
cd '''              #多行字符串用三个单引号或者三个双引号
d = ''              #python 支持空字符串的创建
print(a)
print(b)
print(c)
print(d)

print("转义字符")
#我们通常用\+特殊字符，实现某些难以用字符表示的效果
a = "i\nlove\nyou"  #\n 是换行
print(a)

b = 'I\'m a teacher'   #\' 表示单引号
print(b)

c = ('aaaaaa\
ccccccc')             #\ 续航符

print(c)

print("字符串拼接")
print("aa" + "bb")  #两边是字符串，会拼接，从而形成新的对象
print(3 + 4)        #两边是数字，会相加
print("aa"+ str(3.14))  #两边一边是字符串，一边是数字，需要统一类型str()

a = 'baixiaochun' * 3
print(a)                #字符串复制

print("aa",end="bb\n")
print("bb",end="\n")
print("cc",end="\tdds")   #通过end = "" 进行不换行打印

print("通过控制台读取字符串")
myname = input('您好，请问你叫什么名字：')   #input()从控制台读取键盘输入的内容
print("你好，很高兴认识你,"+myname + "!")



