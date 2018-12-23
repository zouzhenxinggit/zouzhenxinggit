#!/usr/bin/python3
#coding=utf-8



print("make sweetpotato")
'''
cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
cookedString : 这是字符串；描述地瓜的生熟程度
condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
'''

class SweetPotato:

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    def __str__(self):
        msg = "地瓜的生熟程度为:" + self.cookedString + "\t"
        msg += "等级为" + str(self.cookedLevel) + "\t"
        
        if len(self.condiments) > 0 :
            msg += "添加的作料有"
            for tmp in self.condiments:
                msg += tmp + ","
            #msg = msg[:-1:]
            msg = msg.strip(",")    #清楚字符串两头的","
        else :
            msg += "没添加任何作料"
        return msg

    def cook(self, times):
        self.cookedLevel += times;

        if self.cookedLevel > 8:
            self.cookedString = "烤焦了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    def addCondiments(self, Condiments):
        self.condiments.append(Condiments)

potato = SweetPotato()
print(potato)

potato.cook(2)
print(potato)

potato.cook(2)
print(potato)

potato.cook(2)
print(potato)

potato.cook(2)
print(potato)

potato.cook(2)
print(potato)

potato.addCondiments("糖")
print(potato)

potato.addCondiments("醋")
print(potato)

potato.addCondiments("辣椒")
print(potato)

potato.addCondiments("芝麻")
print(potato)