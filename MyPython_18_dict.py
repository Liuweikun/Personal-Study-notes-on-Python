print("字典元素的添加，删除，修改")
a = {"name":"chenyanyu","age":18,"job":"programmer"}

print("添加")
a["address"] = "taiyuan,China"
print(a,"\n")

print("修改")
#相同的项目替换，不相同的项目则显示增加
b = {"name":"qizheyin","age":18,"sex":"woman"}
a.update(b)
print(a,"\n")

print("删除\n")
#del()删除是字典中的元素
#clear()删除的是所有的键值对
#pop()删除指定的键值对，并返还相应的值对象
#popitem() 方法返回并删除字典中的最后一对键和值
del(a["name"])
print(a)
b = a.pop("age")
print(b)     #返还被删除的键值对的值对象
print(a)
a.clear()
print(a)   
a = {"name":"chenyanyu","age":18,"job":"programmer"}
a.popitem()
print(a)
a = {"name":"chenyanyu","age":19,"job":"programmer"}
a.popitem()
print(a)
a = {"name":"chenyanyul","age":18,"job":"programmer"}
a.popitem()
print(a)
a = {"name":"chenyanyul","age":19,"job":"programmer"}
a.popitem()
print(a)
a = {"name":"chenyanyu","age":18,"job":"programmer"}
a.popitem()
a.popitem()
print(a)
#经证明，确实是删除最后的一个键值对


