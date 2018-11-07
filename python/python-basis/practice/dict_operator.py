#!/usr/bin/python3
#coding=utf-8

print("dict常见操作")


info = {"name":"zouzhenxing", "age":105, "sex":"男"}
print(info)


#添加新的字典元素 键值对
info[123] = "hhaa"
print(info)

#修改字典
info["age"] = 109
print(info)

#print(info["xxxxx"]) #报错

#删除字典元素和删除字典
del info["sex"]
print(info)

del info
#print(info)

#"清空字典 并不是删除"
info = {"name":"zouzhenxing", "age":105, "sex":"男"}
info.clear()
print(info)

'''
[(),(),()]
[{},{}]
[[],[]]
'''

info = {"name":"zouzhenxing", "age":105, "sex":"男"}

#测量字典中，键值对的个数
print( len(info) )

#返回一个包含字典所有KEY的列表
print(info.keys())

#返回一个包含字典所有value的列表
print(info.values())

#返回一个包含字典所有key+value的元祖的列表
print(info.items())

#如果key在字典中，返回True，否则返回False python2可以用 python3删除了
#print( info.has_key('age') )
