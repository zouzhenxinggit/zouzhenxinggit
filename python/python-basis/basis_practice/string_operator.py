#!/usr/bin/python3
#coding=utf-8
'''
切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
切片的语法：[起始:结束:步长]
print("python切片")
'''

name = "asdfghjklqwqettuiop"

print(name[0])
print(name[1])

print(name[0:5])
print(name[1:3])
print(name[4:9])
print(name[0:700])
print(name[0:])
print(name[:])

print(len(name))

print(name[::])
print(name[::2])
print(name[::3])
print(name[::-1])
print(name[::-2])
print(name[::1])
print(name[0:5:2])


print("*"*30)
name = 'abcdef'
print(name[::])
print(name[-1])
print(name[-2])

print(name[0:0])
print(name[0:-1])
print(name[0:-2])


print("*"*30)

aStr = "my love is lol and my dnf"

print(aStr.find('my'))
print(aStr.find('lol'))
print(aStr.index('and'))

print(aStr.rfind('my'))
print(aStr.rindex('and'))

#print(aStr.index('andxx')) 如果index没有找到字符串就会爆出一个异常

#取出文件名的后缀
filename = "Zou.txt.exe"
print( filename[filename.find('.') : : ])
print( filename[filename.rfind('.') : : ])


#字符串出现的次数
print( aStr.count('my') )
print( aStr.count('my', 3, len(aStr)) )

#替换字符串 原字符串不改变
print (aStr.replace('my', 'MY'))
print( aStr.replace('my', 'MY', 1))

#切割 跟切片不同 切片是取出一部分 而切割是分隔开
#啥也不加代表只要是空格都干掉
print("*"*20)
print ( aStr.split(' ') )
print ( aStr.split('y') )

aStrr = aStr + "\t \t \t n"
print ( aStrr)
print ( aStrr.split() )


#把第一个字符串的第一个字符大写
print ( aStr.capitalize() )

#把字符串的第一个字符大写
print ( aStr.title() )

#比如检查用户上传的头像是否为jpg格式 就用这个
#检查字符串是否以“XX”开头
print(aStr)
print( aStr.startswith("my"))
print( aStr.startswith('xx') )

#检查字符串是否以“XX”结尾
print( aStr.endswith('dnf') )
print( aStr.endswith('xx') )
print( filename.endswith('.exe') )

nameBS = "TT ss OO pp"
#所有大写字符变成小写
print( nameBS.lower() )
#所有小写字符变成大写
print( nameBS.upper() )


#将字符串左对齐并使用空格填充指定长度的字符串
print ( aStr.ljust(50) , end = "")
print("*")
#将字符串右对齐并使用空格填充指定长度的字符串
print ( aStr.rjust(50) , end = "")
print("*")
#将字符串右居中并使用空格填充指定长度的字符串
print ( aStr.center(50), end = "")
print("*")

aStrip = aStr.center(50)
print(aStrip, end = "")
print("*")

#删除左边空白字符串
print ( aStrip.lstrip() , end = "")
print("*")

#删除右边空白字符串(\t也可以删除掉)
print ( aStrip.rstrip() , end = "")
print("*")

#删除两边空白字符串(\t也可以删除掉)
print ( aStrip.strip() , end = "")
print("*")

#删除两边空白字符串(\t也可以删除掉)
print ( aStrip.strip("my") , end = "")
print("*")

#把字符串切割成三部分 str前 、str 、str后  
#圆括号表示元组 中括号表示 元素列表
print ( aStr.partition("my") )
print ( aStr.rpartition("my") )

mystr = "yes\nyes\nyes"
print(mystr)

#把字符串按照换行分割
print ( mystr.splitlines() )

#判断字符串是否都是由字母组成的(空格不算字母)
aStr2 = "asdasdasdasdflkjfa"
print ( aStr2 )
print ( aStr2.isalpha() )
print ( aStr.isalpha() )

#判断字符串是否都是由数字组成的(空格不算数字)
aStr3 = "12345678"
aStr4 = "123456 78"
print ( aStr3 )
print( aStr3.isdigit() )
print( aStr4.isdigit() )

#判断字符串是否都是由数字和字母组成的(空格不算数字和字母)
aStr4 = "1asdasd56vaskm78"
print( aStr.isalnum() )
print( aStr4.isalnum() )

#如果 mystr 中只包含空格，则返回 True，否则返回 False.
aStr5 = '          '
print( aStr5.isspace() )
print( aStr.isspace() )

#在li这个列表的每个元素后边加上str组成新的字符串
str1 = ' '
str2 = ""
li = ['my', 'name', 'is', 'zou']
print( str1.join(li) )
print( str2.join(li) )

#（面试题）给定一个字符串teststr，返回使用空格或者'\t'分割后的倒数第二个子串
teststr = "haha nihao a \t heihei \t  woshi nide \t hao npengy" 

print(teststr)
print( teststr.split() )
print( teststr.split()[1:4:] )
print( teststr.split()[-2] )
