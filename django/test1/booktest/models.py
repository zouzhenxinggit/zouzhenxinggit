#coding=utf-8

from django.db import models

# Create your models here.

# 表名是类名
class BookInfo(models.Model):
    # 类属性 对应表的图书名称 CharField创建varchar
    btitle = models.CharField(max_length=20)
    # DateField  --- datetime
    # bpub_date = models.DateTimeField()
    bpub_date = models.DateField() #带时间


    def __str__(self):
        # pk 主键
        return self.btitle.encode('utf-8')

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname.encode('utf-8')
