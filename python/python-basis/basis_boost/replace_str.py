#!/usr/bin/python3
#coding=utf-8



print("replace str ")

#请书写一个函数 用于替换一个字符串中的一个或多个字符串

pstr = "hello world! nihao world xxx"

def strreplace(pstr, oldstr, newstr):  
    while True: 
        position = pstr.find(oldstr)
        if position == -1:
            break
        pstr = pstr[:position] + newstr + pstr[position + len(oldstr):]
    return pstr


def strreplace1(pstr, oldstr, newstr):
    return  pstr.replace(oldstr,newstr)


def strreplace3(pstr, oldstr, newstr):

    list = pstr.split(oldstr)
    print(list)
    return newstr.join(list)


afterReplaceStr = strreplace(pstr, "world", "Tom")
print(afterReplaceStr)

afterReplaceStr1 = strreplace1(pstr, "world", "Tom")
print(afterReplaceStr1)

afterReplaceStr3 = strreplace3(pstr, "world", "Tom")
print(afterReplaceStr3)

