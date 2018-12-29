#!/usr/bin/python3
#coding=utf-8



print("factory_method")



class Carshop(object):

    def createcar(self):
        pass

    def order(self, typename):
        self.car = self.createcar(typename)

        self.car.move()



#父类接口函数 子类实现


class Dazhong(object):
    def move(self):
        print("Dazhong move")

class Yiqi(object):
    def move(self):
        print("Yiqi move")


class CarStore(Carshop):

    def createcar(self,typename):
        self.carfactory = Carfactory()
        return self.carfactory.back_car(typename)


class Carfactory(object):
    def back_car(self, typename):
        if typename == "Dazhong":
            car = Dazhong()
        elif typename == "Yiqi":
            car = Yiqi()
        return car
            

car = CarStore()
car.order("Yiqi")
