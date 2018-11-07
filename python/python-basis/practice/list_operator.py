#!/usr/bin/python3
#coding=utf-8

print("list 元素列表的增删改")


alist = ["xiaohong","xiaozhen","xiaowei"]
print(alist)

#通过append可以向列表添加元素
alist.append("xiaoyue")
print(alist)

#在指定位置index前插入元素object
#insert(index, object) 
alist.insert(0, "xiaofei")
alist.insert(3, "xiaoxing")
print(alist)

#通过extend可以将另一个集合中的元素逐一添加到列表中
blist = ["aaa","bbb"]
alist.extend(blist)
print(alist)

#将元素列表当成一个整体添加到另一个元素列表当中
alist.append(blist)
print(alist)

print(alist[5])
print(alist[-1])
print(alist[-2])
print(alist[-1][0])
print(alist[-1][1])

alist.insert(0, blist)
print(alist)

print(alist[1][0])
print(alist[1][1])
print(alist[1][2])

#改
alist[2] = "123123"
alist[-1][1] = "cc" #实际上是修改了blist 所以前后都跟着变化
alist[-1][0] = 'dacd'
print(alist)

#查 in not in roster.py
#	if each_name in  roster1:
#	if each_name not in  roster1:

print ( alist.count("xiaofei") ) #出现次数
print ( alist.count("xiaohong") )
print ( alist.count(blist) )

print ( alist.index("xiaofei") ) #返回索引
print ( alist.index("xiaowei") )
#print ( alist.index("xiaohong") )
print ( alist.index(blist) )

#删除
'''del：根据下标进行删除
pop：删除最后一个元素
remove：根据元素的值进行删除'''

print ( alist )
del alist[1]
del alist[2]
print ( alist )

alist.pop()
print ( alist )
alist.pop()
print ( alist )

alist.remove("xiaoyue") #没有的话就显示错误
print ( alist )

#排序
name1 = [1,8,6,2,5,3,4,7]

#逆序
name1.reverse()
print ( name1 )

name1.sort()
print ( name1 )

#big -> small 
name1.sort(reverse = True)
print ( name1 )

name1.sort(reverse = False)
print ( name1 )