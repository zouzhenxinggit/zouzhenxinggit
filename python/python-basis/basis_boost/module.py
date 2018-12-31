#!/usr/bin/python3
#coding=utf-8

print("main.py")

'''
当你导入一个模块，Python解析器对模块位置的搜索顺序是：

当前目录
如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。 echo $PATH
如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
'''

#添加自定义模块路径
import sys
print(sys.path)
sys.path.append("/home/zouzhenxing/zouzhenxing_study_project/python/python-basis/basis_boost/Module")
print(sys.path)

#添加模块 添加模块的时候就相当于执行一遍这个模块的py文件
import time
from myself_module import *
#*代表了myself_module模块中的__all__ 

a = Class_test()
a.printf()

test1()

#test2()	all中没有test2 可以再添加
from myself_module import test2
test2()