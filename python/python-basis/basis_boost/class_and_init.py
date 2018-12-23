#!/usr/bin/python3
#coding=utf-8



print("class make")

#定义一个类
class cat:
    #属性

    #行为
    def __init__(self,newcloor,newhigh): #自动调用
        print("__init__行为")
        self.collor = newcloor
        self.high = newhigh
        self.dollor = "100$"

    def eat(self,a,b):
        print("---eat---")
        print("a=%d b=%d" %(a,b))

    def drink(self):
        print("---drink---")

    def print_info(self):
        print(self.collor)
        print(self.high)



#定义对象     调用对象的行为
hellocat = cat("黑色", 50)
hellocat.print_info()
hellocat.eat(1,2)
hellocat.drink()

#给类添加属性
hellocat.collor = "白色"
hellocat.high = 20 #cm

#获取类的属性 2种方法
print( hellocat.collor )
print( hellocat.high )
hellocat.print_info()

































