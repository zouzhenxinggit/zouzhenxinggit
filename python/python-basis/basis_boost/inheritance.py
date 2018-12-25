#!/usr/bin/python3
#coding=utf-8



print("private")


class Cat(object):
   
    def __del__(slef):
        print("------cat------")

    def __init__(self):
        self.__name = "mao"

    def print_selt(self):
        print("--猫--")

    def __test(self):
        print("----")


class Bosi(Cat):
    '''
    #不能调用父类的私有属性
    def test(self):
        self.__test()
        print(self.__name)
    ''' 
    

class Jiafei(Cat):
    pass

bosi = Bosi()
jiafei = Jiafei()

bosi.print_selt()
jiafei.print_selt()


#bosi.test()