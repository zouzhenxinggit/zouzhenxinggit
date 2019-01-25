#coding=utf-8

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# IPython imports
from MysqlHelper import *
from RedisHelper import *
from hashlib import sha1



#登录redis
def redis_login():
    return RedisHelper()

#在redis中查询
def redis_query(redis, key):
    return redis.exists(key)

#在redis中读取
def redis_read(redis, key):
    return redis.get(key)

# 在redis中写入
def redis_write(redis, key, value):
    redis.set(key, value)

#连接数据库
def mysql_connection():
    return MysqlHelper("localhost", 3306, "study", "zouzhenxing", "zouzhenxing")

#在mysql中查询是否拥有用户名
def mysql_query(mysql, params):
    sql = 'select name from userinfos where name = %s'
    result = mysql.fetchall(sql, params)

    #print result
    if result == None:
        return False
    elif result[0][0] == params:
        # print result[0][0]
        return True

#在mysql中根据用户名读取密码
def mysql_read(mysql, params):
    sql = 'select pwd from userinfos where name = %s'
    return mysql.fetchone(sql, params)

#注册
def mysql_registered(mysql, uname, upwd):
    sql='insert into userinfos(name,pwd) values(%s,%s)'
    params = [uname, upwd]

    rows = mysql.insert(sql, params)
    print rows

#登录
def login(redis, mysql, uname, upwd2):
    if redis_query(redis, uname):
        print "There is data in redis, Take out the data"
        result = redis_read(redis, uname)
        if result == upwd2:
            print "login succeed"
        else:
            print "password err"
    else:
        print "There is no data in redis, goto database "
        if mysql_query(mysql, uname):
            print "用户名已在数据库注册"
            result = mysql_read(mysql, uname)
            if result[0] == upwd2:
                print "login succeed"
                redis_write(redis, uname, upwd2)
            else:
                print "password err"
        else:
            print "用户名未在数据库注册"

def main():

    result = raw_input("registerer:1 login:2 \n")
    uname = raw_input("请输入用户名：")
    upwd = raw_input("请输入密码：")

    s1 = sha1()
    s1.update(upwd)
    upwd2 = s1.hexdigest()

    redis = redis_login()
    mysql = mysql_connection()

    #注册
    if result == '1':
        mysql_registered(mysql, uname, upwd2)
    # 登录
    elif result == '2':
        login(redis, mysql, uname, upwd2)
    else:
        print "invalid"

main()