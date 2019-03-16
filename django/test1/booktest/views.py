#coding=utf-8

from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from models import *

# Create your views here.

def index(request):
    # # 加载html
    # temp = loader.get_template('booktest/index.html')
    # # 渲染
    # xr = temp.render()
    # return HttpResponse(xr)

    list = BookInfo.objects.all()
    context = {"list": list}

    return render(request, 'booktest/index.html', context)

def zouzhenxing(HttpRequest):
    return HttpResponse('<b> zouzhenxing </b>')

def show(request, id):
    book = BookInfo.objects.get(pk = id)
    herobook = book.heroinfo_set.all()

    context = {'list': herobook}
    return render(request, 'booktest/show.html', context)
