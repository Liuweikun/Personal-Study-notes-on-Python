print("表格练习，使用字典和列表存储，并实现访问")
r1 = {"name":"chenynayu","age":18,"job":"As My first love","city":"北京"}
r2 = {"name":"caoyaxiong","age":18,"job":"As My second love","city":"上海"}
r3 = {"name":"qizheyin","age":18,"job":"As My third love","city":"广州"}
tb = [r1,r2,r3]
print(tb)
print("想要获得第三行人所在的城市\n",tb[2].get("city"))
print("\n打印表中所有信息 ")
for i in range(len(tb)):
    c = tb[i].get("name"),tb[i].get("age"),tb[i].get("job"),tb[i].get("city")
    print(c)

print("\n字典核心底层原理")
#字典的核心是散列表，散列表是一个稀疏数组（总有空白元素的数组）

r1 = {"name":"chenynayu","age":18,"job":"As My first love","city":"北京"}
h1 = bin(hash("name"))   #通过哈希方法获得键对象的哈希值，
print(h1)

#后续需要仔细研究字典核心





