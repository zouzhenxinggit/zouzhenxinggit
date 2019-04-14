#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request,p1):
    return HttpResponse(p1)

def show(request,p1,p2):
    return HttpResponse("%s-%s" %(p1, p2))

def mygod(request,p1,p2,p3):
    return HttpResponse("%s-%s-%s" %(p1, p2, p3))




def getTest1(request):
    return render(request, 'booktest/getTest1.html')

def getTest2(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    context = {'a': a, 'b': b, 'c': c}
    return render(request, 'booktest/getTest2.html', context=context)

def getTest3(request):
    a = request.GET.getlist('a')
    a1 = request.GET['a']
    b = request.GET['b']
    context = {'a': a, 'b': b, 'a1': a1}
    return render(request, 'booktest/getTest3.html', context=context)



def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST.get('uname')
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {
        'uname': uname,
        'upwd': upwd,
        'ugender': ugender,
        'uhobby': uhobby,
    }
    return render(request, 'booktest/postTest2.html', context=context)




# HttpResponse对象
def index1(request):
    t1 = loader.get_template('booktest/index.html')
    context = RequestContext(request, {'h1': 'hello'})
    return HttpResponse(t1.render(context))

#设置cookie和查询cookie
def cookies_test(request):
    response = HttpResponse()
    if request.COOKIES.has_key('h1'):
        response.write('<h1>' + request.COOKIES['h1'] + '<h1/>')
    # response.set_cookie('h1', 'zouzhenxing')
    return response


#重定向    子类HttpResponseRedirect服务器端跳转
def index2(request):
    # return HttpResponseRedirect('/booktest/index3')
    return HttpResponseRedirect('index3')
def index3(request):
    return HttpResponse('<h1> zouzhenxing <h1/>')

# 子类JsonResponse
def json(request):
    return JsonResponse({'list': 'list'})