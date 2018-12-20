#!/usr/bin/python3
#coding=utf-8

print("复制练习.")

#编写复制文件的过程 text.txt text[复制].txt



#打开要两个文件 把文件名字搞定
str_read = input("请输入要复制的文件名")
str_write = str_read[:str_read.find("."):] + "[复制]" + str_read[str_read.find(".")::]

f_read = open(str_read,"r")
f_write = open(str_write,"w")

#读取文件信息 写到结果文件
#第一种
#f_write.write( f_read.read() )
#第二种
#for lineContent in f_read.readlines():
    #f_write.write( lineContent )
#第三种
while True:
    lineContent = f_read.readline()
    if len( lineContent ) > 0:
        f_write.write( lineContent )
    else :
        break

#关闭两个文件
f_write.close()
f_read.close()