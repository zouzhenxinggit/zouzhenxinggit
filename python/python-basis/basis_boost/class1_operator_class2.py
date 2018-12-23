#!/usr/bin/python3
#coding=utf-8




print("home + bed")


class Home:
    def __init__(self, area):
        self.area = area
        self.containsItem = []
        self.light = "on"

    def __str__(self):
        msg = "当前可用面积为" + str(self.area)
        if len(self.containsItem) > 0:
            msg += "\t"
            msg += "家里的物品有"
            for tmp in self.containsItem:
                msg += tmp.getName() + ","
        else :
            msg += "\t"
            msg += "家里啥也没有"
        msg = msg.strip(",")

        msg += "\n"
        if self.light == "on":
            msg += "当前灯是开着灯，所有的物品都是可见的"
        else:
            msg += "当前灯是关着的"
        return msg

    #容纳物品
    def addItem(self, Item):
        needArea = Item.getArea()
        if self.area > needArea:
            self.containsItem.append(Item)
            self.area -= needArea

    def turnoff(self):
        self.light = "off"
        for tmp in  self.containsItem:
            tmp.turnoff()


class Bed:
    def __init__(self, name, area):
        self.area = area
        self.name = name
        self.light = "on"

    def __str__(self):
        msg = self.name + "当前可用面积为" + str(self.area)
        msg += "\t"
        
        msg += "当前的可见度为:" + self.light
        return msg


    #得到面积
    def getArea(self):
        return self.area

    #得到床的名字
    def getName(self):
        return self.name

    def turnoff(self):
        self.light = "off"


home = Home(128)
print(home)


bed1 = Bed("席梦思", 4)
print(bed1)

bed2 = Bed("硬板床", 3)
print(bed2)

home.addItem(bed1)
print(home)

home.addItem(bed2)
print(home)

print("================分割线=================")
home.turnoff()
print(home)
print(bed1)
print(bed2)