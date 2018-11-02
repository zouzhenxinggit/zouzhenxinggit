#!/usr/bin/python3
#coding=utf-8

print("operator", end = " text\n")

a = 10
b = 2
c = 10.0
d = 11
e = 11.0


print("a = %d" %a)
print("b = %d" %b)
print("c =", c)
print("d = %d" %d)
print("e =",e)

print("------------------------------------")
print("a+b = %d" %(a+b))
print("a-b = %d" %(a-b))
print("a*b =", a*b)
print("------------division----------------")

print("a/b =", a/b) 	#5.0
print("a/b = %d" %(a/b)) 	#5   看你怎么用了 %d就是整数 %f就是浮点数
print("a/b = %f" %(a/b)) 
print("a/3 = ", (a/3))		#3.3333
print("a//b = ", a//b) 	#3.3333
print("a//3 = ", a//3) 		#3
print("a%3 = ", a%3) 		#1

'''
/正常的除法 得到什么是什么 能除开就除开  除不开小数点该是多少位就是几位
//取除法结果的整数
%取余
'''
print("------------------------------------")
print("a+c/b", a+c/b) #15.0
print("(a+c)/b", (a+c)/b) #10.0

print("------------------------------------")
print("a**4 ", a**4)

print("*"*30)
aa = a+b
print("aa = a + b %d" %aa)


print("------------------------------------")
a , b = 20, 30
print("a = %d b = %d" %(a,b))
a,b = b , a
print("a = %d b = %d" %(a,b))

a+=1
print("a+=1: a = %d" %a)
a-=1
print("a-=1: a = %d" %a)
a*=2
print("a*=2: a = %d" %a)
a/=2
print("a/=2: a = %d" %a)
a//=7
print("a//=7: a = %d" %a)
a%=7
print("a%=7: a =",a)
a*=2
print("a*=2: a = %d" %a)
a**=2
print("a**=2: a = %d" %a)

a*= 3+4-6
print("a*= 3+4-6: a = %d" %a)

