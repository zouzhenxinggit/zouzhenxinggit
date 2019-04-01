from django.shortcuts import render
from models import *
from django.db.models import Max,Avg,Count,Min,Sum,F,Q

# Create your views here.

def index(request):

    max_bpub_date =  BookInfo.books2.aggregate(Max('bpub_date'))
    context = {'list': max_bpub_date}
    return render(request, 'bookinfo/index.html', context)


# def show(request, id):
#     book = BookInfo.objects.get(pk=id)
#     herobook = book.heroinfo_set.all(
#     context = {'list': herobook}
#     return render(request, 'booktest/show.html', context)

