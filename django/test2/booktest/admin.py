#coding=utf-8

from django.contrib import admin
from models import BookInfo
from models import HeroInfo

# Register your models here.



# 这个文件 站点管理 用户管理

class HeroInfoInline(admin.StackedInline):
    # 可以将内嵌的方式改为表格 上面是列表
    # class HeroInfoInline(admin.TabularInline)
    # 关联类
    model = HeroInfo
    # 关联类个数
    extra = 1



# 自定义管理页面来定义模型在Admin界面的显示方式
class QuestionAdmin_BookInfo(admin.ModelAdmin):
    # 用列表去显示BookInfo属性
    list_display = [
        'pk',
        'btitle',
        'bpub_date',
        'bread',
        'bcommet',
        'isDelete',
    ]

    # 过滤字段 过滤框会出现在右侧
    list_filter = [
        'btitle',
        'bpub_date',
        'bread',
        'bcommet',
        'isDelete',
    ]

    # 搜索字段 搜索框会出现在上侧
    search_fields = ['btitle']

    # 分页每页显示多少
    list_per_page = 10

    # 属性的先后顺序
    # fields = ['bpub_date', 'btitle']

    # 属性分组
    fieldsets = [
        # ('base', {'fields': ['btitle']}),
        # ('super', {'fields': ['bpub_date']})
        ('basic', {'fields': ['btitle', 'bpub_date']}),
        ('more', {'fields': ['bread', 'bcommet', 'isDelete',]}),
    ]

    # 新建关联类
    inlines = [HeroInfoInline]

# Register your models here.
# 向admin注册booktest的模型 将来就可以用站点管理去新建对象 创建对象就和数据库挂钩
admin.site.register(BookInfo, QuestionAdmin_BookInfo)




class QuestionAdmin_HeroInfo(admin.ModelAdmin):
    # 用列表去显示HeroInfo属性
    list_display = [
        'pk',
        'hname',
        'hgender',
        'isDelete',
        'hcontent',
        'hbook',
    ]

    # 过滤字段 过滤框会出现在右侧
    list_filter = [
        'hname',
        'hgender',
        'isDelete',
        'hcontent',
        'hbook',
    ]

    # 搜索字段 搜索框会出现在上侧
    search_fields = ['btitle']

    # 分页每页显示多少
    list_per_page = 10

    # 属性的先后顺序
    # fields = ['bpub_date', 'btitle']

    # 属性分组
    fieldsets = [
        # ('base', {'fields': ['btitle']}),
        # ('super', {'fields': ['bpub_date']})
        ('basic', {'fields': ['hname', 'hgender']}),
        ('more', {'fields': ['hcontent', 'hbook', 'isDelete',]}),
    ]

admin.site.register(HeroInfo, QuestionAdmin_HeroInfo)
