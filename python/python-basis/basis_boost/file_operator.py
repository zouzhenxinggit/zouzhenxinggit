#!/usr/bin/python3
#coding=utf-8

import os

print("复制练习..")


'''获取当前读写的位置tell
定位到某个位置seek(offset, from)
offset:偏移量
from:方向
0:表示文件开头
1:表示当前位置
2:表示文件末尾
'''


f = open("abc.txt", "w+")
f.write("hahhaha")

f.seek(3 ,0)
print( f.tell() )
print( f.read() )
f.close()

print("*"*10)
#文件的重命名和删除

os.rename("abc.txt", "cba.txt")
os.remove("cba.txt")

print("*"*10)
#文件的其他相关操作
#创建文件夹
os.mkdir("zhangsan")
#获取当前目录
print( os.getcwd() )
#改变默认目录
os.chdir("/")
print( os.getcwd() )
#获取目录列表
print( os.listdir() )
#删除文件夹
os.rmdir("/home/zouzhenxing/zouzhenxing_study_project/python/python-basis/basis_boost/zhangsan")
