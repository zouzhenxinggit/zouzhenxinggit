#!/usr/bin/python3
#coding=utf-8



print("factory_pattern")


class Cake(object):
    
    def cake(self):
        print("这是一个蛋糕")


class Sweetcake(Cake):

    def caketaste(self):
        print("这是一个甜蛋糕")
    

class Saltycake(Cake):
   def caketaste(self):
        print("这是一个咸蛋糕")


class Cakefactory(object):
    
    def create_creake(self, typename): 
        if typename == "sweet":
            return Sweetcake()
        elif typename == "salty":
            return Saltycake()

class Cakeshop(object):

    def __init__(self):
        self.cakefactory = Cakefactory()

    def order(self,typename):
        cake = self.cakefactory.create_creake(typename)
        
        cake.caketaste()
        cake.cake()

cake = Cakeshop()
cake.order("sweet")
cake.order("salty")