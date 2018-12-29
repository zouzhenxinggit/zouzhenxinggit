#!/usr/bin/python3
#coding=utf-8



print("singleton_pattern")



class King(object):
    
    __instance = None
    __first_init = False
    wocao = 11

    def __new__(cls,age,name):
        if not cls.__instance: 
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,age,name):
        
        ''' 
        self.__first_init = True
        print("self.__first_init",self.__first_init)
        print("King.__first_init" ,King.__first_init)
        while True:
            pass
        '''
        if not King.__first_init:      
        #在这里self.__first_init不太好  
        #如果没定义了self.__first_init 那就会调用类属性 
        #如果定义了 self.__first_init 那不会访问类属性 这是假象。。
            self.name = name
            self.age = age
            King.__first_init = True

    
    def printf(self):
        print(self.age)
        print(self.name)
        print(self.__first_init)
 
a = King(18,"laowang")
print(a)


b = King(19,"laosong")
print(b)
b.printf()
a.printf()