#!/usr/bin/python3
#coding=utf-8

print("cycle_change_lotsof_file_name")


import os

print("cycle_change_lotsof_file_name")


#新建一个目录 然后进入这个目录
os.mkdir("cycle")

dir_str = os.getcwd() + "/cycle"
print( dir_str )

os.chdir( dir_str )
print( os.getcwd() )

#创建文件 新三国-1.txt ... 新三国-9.txt

i  = 1
while i < 9 :
    fstr = "新三国" + str(i) + ".txt"
    f = open(fstr, "w+")
    f.close()
    i += 1

#循环重命名文 [dongge]新三国-1.txt ... [dongge]新三国-9.txt
dongge_str = os.listdir()
print( dongge_str )

for n,tmp in enumerate(dongge_str):
   new_fname = "[dongge]" + tmp
   os.rename(tmp, new_fname)
