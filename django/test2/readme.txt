
setting设置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test2',
        'USER': '用户名',
        'PASSWORD': '密码',
        'HOST': '数据库服务器ip，本地可以使用localhost',
        'PORT': '端口，默认为3306',
    }
}

编写modles文件
生成偏移
执行偏移
去数据库中查看

insert into bookinfo(btitle,bpub_date,bread,bcommet,isDelete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0)






创建模型类对象(模型类和管理类中不能调用__init__()方法)






数据库和modles模块交互通过manager管理器交互
管理器映射了数据库和模型类
管理器对象一般作为模型类的类方法实现映射

默认objects：是Manager类型的对象，用于与数据库进行交互

也可以重写管理器 重写管理器默认的objects就会没有
通过重写get_query()方法   get_query() BookInfo.books2.all就会返回相应的条件所有的数据库对象
也就是all过滤器会调用get_query方法

2种方法(推荐第一种)
在管理类中定义
    # 自定义创建模型类对象方法
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
在模型类中定义
    # 自定义创建模型类对象方法
    @classmethod
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

测试
python2.7 manage.py shell

from datetime import datetime

from booktest.models import BookInfo

b = BookInfo.books2.create("abc", datetime(2019,3,19))

b = BookInfo.create("abc", datetime(2019,3,19))

保存的话直接b.save()



查询


查询返回的数据叫查询集
查询的方法叫过滤器




[16:46]@-Inspiron-3543:~/zouzhenxing_study_project/django/test2$ python2.7 manage.py createsuperuser
Username (leave blank to use 'zouzhenxing'): zouzhenxing
Email address: zouge666666
Error: Enter a valid email address.
Email address: zouzhenxing.it@foxmail.com
Password:
Password (again):
Superuser created successfully.








#coding=utf-8

from django.db import models

# Create your models here.

# 通过重写管理器manager类里的get_queryset方法去实现查询
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(id=3)#isDelete=False)

    # 自定义创建模型类对象方法
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b



class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table = 'bookinfo'
        # ordering = ['id']
        # ordering = ['-id']

    # 默认定义管理类对象
    books1 = models.Manager()

    # 自定义管理类对象
    books2 = BookInfoManager()

    @classmethod
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')