#coding=utf-8

from django.db import models

# Create your models here.

class BookInfo_Manager(models.Manager):
    def get_queryset(self):
        return super(BookInfo_Manager, self).get_queryset().filter(isDelete = False)

    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False


class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table = 'BookInfo'

    books1 = models.Manager()
    books2 = BookInfo_Manager()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
    class Meta():
        db_table = 'HeroInfo'