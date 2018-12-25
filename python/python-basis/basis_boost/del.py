#!/usr/bin/python3
#coding=utf-8



print("private")


#__name __私有变量 不能在外部直接调用 内部函数可以调用
#__func __私有函数 不能在外部直接调用 内部函数可以通过self.__(xx)调用
class private:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __del__(slef):
        print("------del------")

laowang = private("laowang",18)
del laowang



laowang = private("laowang",20)
laozhang = laowang

del laowang
print(laozhang)
del laozhang

#多个变量指向对象(并不是复制多个对象) 这里有一个引用计数器的存在 记录有几个变量引用这个内存空间
#当引用计数器 = 0时 调用__del__

'''
总结

当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，即变为2，
当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''