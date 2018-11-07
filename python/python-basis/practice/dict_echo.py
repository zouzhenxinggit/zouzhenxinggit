#!/usr/bin/python3
#coding=utf-8

print("dict traverse")


info = {"name":"zouzhenxing","sex":"nan","age":23}
print(info)

for tmp in info.keys() :
	print(tmp)

for tmp in info.values() :
	print(tmp)

for tmp in info.items() :
	print(tmp)

for tmp in info.items() :
	print(tmp[0])
	print(tmp[1])

for tmp in info.items() :
	print("%s:%s" %(tmp[0], tmp[1]))

for key,value in info.items() :
	print("%s:%s" %(key,value))


#实现带下标索引的遍历
i = 0
for key,value in info.items() :
	print("%d %s:%s" %(i, key,value))
	i += 1


#enumerate()
for i, tmp in enumerate(info.items()) :
	print("%d %s:%s" %(i, tmp[0], tmp[1]))

charq = ["a",'b','c','d']

for i,tmp in enumerate(charq) :
	print (i, tmp)


#other + * 运算符的重载

print( "aaa" + "bbb" )
#print( ["aaa","ccc"] + "bbb" ) error
print( ["aaa","ccc"] + ["nnn","mmm"] ) 
print( ["aaa","ccc"] * 2 ) 

print("-"*50)


aa = [11,22,33,44,55]
print( min(aa) )
print( max(aa) )

#删除变量 del(info) or del info
#比较两个值  cmp(item1, item2)