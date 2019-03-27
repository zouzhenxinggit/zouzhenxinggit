django我操作的知识点


分成三大部分
视图 模块 模板
MVT



创建项目
django-admin startproject test1

__init__.py 把目录编看成包

setting.py 配置   DATABASES 配置数据库
urls.py 项目URL声明
wsgi.py 项目与WSGI兼容的Web服务器入口



创建应用
在一个项目中可以创建一到多个应用，每个应用进行一种业务处理
python2.7 manage.py startapp booktest


打开models.py文件，定义模型类
定义好之后
编辑settings.py文件，将booktest应用加入到installed_apps中

生成迁移文件
迁移文件就是对应真实数据库的一种方法
python2.7 manage.py makemigrations

执行迁移执行之后 数据库和对象就绑定在了一起
python2.7 manage.py migrate

测试数据操作
进入python shell 进行简单的模型API练习
python2.7 manage.py shell
接着
from booktest.models import BookInfo,HeroInfo
from datetime import *

新建图书信息 创建数据库中的内容
b = BookInfo()
b.btitle="shediao"
b.bpub_date=datetime(year=1990,month=1,day=10)
b.save()

查询
BookInfo.objects.all()
BookInfo.objects.all()[0].btitle
BookInfo.objects.all()[0].bpub_date

条件查询
BookInfo.objects.get(b.id=2)  ..id=1

 修改图书信息：
b.btitle=u"天龙八部"
b.save()

删除图书信息：
b.delete()
BookInfo.objects.all()[0].delete()


关联对象的操作
h=HeroInfo()
h.hname=u'郭靖'
h.hgender=True
h.hcontent=u'降龙十八掌'
h.hBook=b
h.save()

获得关联集合：返回当b对象的所有hero
b.heroinfo_set.all()

c=b.heroinfo_set.create(htitle=u'黄蓉',hgender=False,hcontent=u'打狗棍法')
print c














用django的管理
创建一个管理员用户
python manage.py createsuperuser

关联对象
关联注册
在新建对象的同时直接关联子对象


视图
网页显示

模板
