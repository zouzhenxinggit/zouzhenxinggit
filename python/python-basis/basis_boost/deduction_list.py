#!/usr/bin/python3
#codinf=utf-8

print("deduction list")

#列表推导式

a = range(0,10) #0-9
print(a)

#推导0-9的列表
tmp = [x for x in range(0,10)]
print(tmp)

#range步长
tmp_long = [x for x in range(1,10,2)]
print(tmp_long)

#推导0-9的列表 偶数
#1满足条件X进入list 2range步长 都可以 
tmp_o = [x for x in range(0,10) if x%2 == 0]
tmp_o = [x for x in range(0,10,2)]
print(tmp_o)

#重复循环推到列表 
tmp_cycle = [x for x in range(0,4) for y in range(0,2)]
print(tmp_cycle)

#类似坐标 两个for循环
tmp_xy = [(x,y) for x in range(0,4) for y in range(0,2)]
print(tmp_xy)

#三个for循环
tmp_xyz = [(x,y,z) for x in range(0,4) for y in range(0,2) for z in range(7,9)]
print(tmp_xyz)