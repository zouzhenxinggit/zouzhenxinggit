#!/usr/bin/python3
#coding=utf-8

print("字典里存放键值对")

#key键 value值
#info = {key:value} key的值不可以重复 根据ker寻找value

info = {"name":"zouzhenxing", "age":22, "wife":"吴秀婷",}

print(info)

print(info["name"])
print(info["age"])
info["age"]=23
print(info["age"])

#如果字典里没有的话就会错误 
#print(info["age000"])

#key不可以重复 定义时候覆盖掉
info = {"name":"zouzhenxing", "age":22, "wife":"吴秀婷", "wife":"吴秀婷123"}
print(info)

#返回None说明没有 没有的话还可以添加一个默认值
print(info.get("aegoto")) 
print(info.get("aegoto","不知道"))
print(info.get("aegoto",180))
print(info)
