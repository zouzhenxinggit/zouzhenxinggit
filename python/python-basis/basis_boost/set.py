#!/usr/bin/python3
#codinf=utf-8

print("set list tuple conversion")


#set 集合  不准许有重复元素

a = [11,22,33,44,33,22,11]
b = set(a)
print(a,b)

c = tuple(a)
d = tuple(b)
print(c,d)

e = list(b)
f = list(a)
g = list(c)
print(e,f,g)

#三者可以相互转换
