#!/usr/bin/python3
#coding=utf-8



print("str_self make")


class dog:      #这个类里的self是这个意思 wangcai.print_info() 相当于print_info(wangcai) 作用也就是this指针
    def __init__(self, color):
        self.color = color

    def print_info(self):
        print( self.color )
    
    def __str__(self):
        return "颜色是" + self.color


wangcai = dog("bai")
print( wangcai.color )


gousheng = dog("hei")
print( gousheng.color )


def test(AAA):
    AAA.print_info()

test(wangcai)


print(wangcai)  #打印类名以及对象地址 == id(对象) 
print(gousheng)
print(id(wangcai))      
print(id(gousheng))























