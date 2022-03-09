print("嵌套函数")
#在函数内部定义的函数


def outer():
    print("outer running")

    def inner():
        print("innter running")

    inner()

outer()
#嵌套函数好处在于可以隐藏很多内部的细节
#1.封装-数据隐藏，外部无法访问嵌套函数
#2.贯彻DRY原则，可以让我们在函数内部避免重复代码
#3.闭包