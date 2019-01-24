#coding=utf-8

"""

create table userinfos(
id int not null primary key auto_increment,
name varchar(20),
pwd char(40),
idDelete bit default 0
);
请输入用户名：zouzhenxing
请输入密码：zouzhenxing

"""

from MysqlHelper import *
from hashlib import sha1


# #注册
# uname = raw_input("请输入用户名：")
# upwd = raw_input("请输入密码：")
#
# s1 = sha1()
# s1.update(upwd)
# upwd2 = s1.hexdigest()
#
# sql='insert into userinfos(name,pwd) values(%s,%s)'
# params = [uname, upwd2]
#
# mysql = MysqlHelper("localhost", 3306, "study", "zouzhenxing", "zouzhenxing")
# rows = mysql.insert(sql, params)
# print rows

#登录
uname = raw_input("请输入用户名：")
upwd = raw_input("请输入密码：")

s1 = sha1()
s1.update(upwd)
upwd2 = s1.hexdigest()

sql1 = "select pwd from userinfos where name = %s"
params = [uname]

mysql = MysqlHelper("localhost", 3306, "study", "zouzhenxing", "zouzhenxing")
result = mysql.fetchone(sql1, params)

if result == None:
    print '用户名错误'
elif result[0] == upwd2:
    print '登录成功'
else:
    print '密码错误'








































