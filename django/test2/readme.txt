
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

BookInfo.books2.all()

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


查询集 和 过滤器 基于管理器

通过过滤器查询的结果叫查询集
过滤器
all() 查询所有 all就调用了管理器的get_queryset方法
filter() 过滤
BookInfo.books2.filter(isDelete = 0, id = 2)
exclude() 反过滤
BookInfo.books2.exclude(isDelete = 0, id = 2)
order_by() 排序
BookInfo.books1.order_by()
values() 一个对象返回成一个字典 用列表返回
BookInfo.books1.values()


返回单个值的方法
get()：返回单个满足条件的对象
如果未找到会引发"模型类.DoesNotExist"异常
如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常
count()：返回当前查询的总条数
BookInfo.books2.count()
first()：返回第一个对象
BookInfo.books2.first()
last()：返回最后一个对象
BookInfo.books2.last()
exists()：判断查询集中是否有数据，如果有则返回True
BookInfo.books2.exists()

限制查询集
BookInfo.books1.filter()[0:1].get()

查询集的缓存
查询集是有缓存的

字段查询
判断等于 大小写敏感 可以省略
keyushengluelter(isDelete__exact=0)
判断包含 大小写敏感
BookInfo.books2.filter(btitle__contains = '八')
以value开头或结尾 大小写敏感
startswith endswith
BookInfo.books2.filter(btitle__startswith = '天')
BookInfo.books2.filter(btitle__endswith = '传')
是否为null
isnull isnotnull
BookInfo.books2.filter(btitle__isnull = False)
BookInfo.books2.filter(btitle__isnull = True)

在前面加个i表示不区分大小写 如iexact icontains istarswith iendswith

in：是否包含在范围内
BookInfo.books2.filter(id__in = [1,2,3,4,5,6])
大于 大于等于 小于 小于等于 不等于
gt gte lt lte
对日期间类型的属性进行运算
year month day week_day hour minute second：
BookInfo.books2.filter(bpub_date__year = 1980)
BookInfo.books2.filter(bpub_date__gt = datetime(1995,4,1))

BookInfo.books2.filter(heroinfo__hcontent__contains='八')
pk = id
BookInfo.books2.filter(pk = 3)

聚合 F Q
from django.db.models import Max ,F ,Q
Avg,Count,Max,Min,Sum

F 可以使用模型的字段A与字段B进行比较
BookInfo.books2.aggregate(Count('bpub_date'))
BookInfo.books2.aggregate(Max('bpub_date'))
BookInfo.books2.filter(heroinfo__pk__lt = F('bread'))

Q 需要进行or查询，使用Q()对象
BookInfo.books2.filter(Q(pk__gt = 2) & Q(isDelete=False)) 可以简写filter(xx,xx)
BookInfo.books2.filter(Q(pk__gt = 2) | Q(isDelete=False))

&|~结合括号进行分组 构造复杂的Q对象
BookInfo.books2.filter(~Q(pk__gt = 1))